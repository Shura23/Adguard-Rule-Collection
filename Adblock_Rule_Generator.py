import os
import sys
import subprocess
import warnings
import importlib.util
import logging
import asyncio
import aiohttp
import re
import time
from urllib3.exceptions import InsecureRequestWarning
from datetime import datetime, timezone, timedelta

# 设置日志配置，日志文件名为'adblock_rule_downloader.log'，日志级别为INFO
logging.basicConfig(filename='adblock_rule_downloader.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def install_packages(packages):
    # 检查并安装所需的Python包
    for package in packages:
        # 如果包未安装，则安装该包
        if importlib.util.find_spec(package) is None:
            logging.info(f"Package '{package}' is not installed. Installing...")
            subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
            logging.info(f"Package '{package}' installed successfully.")
        else:
            logging.info(f"Package '{package}' is already installed.")

# 要确保安装的包列表
required_packages = ["aiohttp", "urllib3", "certifi"]

# 安装所需的包
install_packages(required_packages)

# 忽略不安全请求警告
warnings.simplefilter('ignore', InsecureRequestWarning)

# 判断是否为有效规则的行，去除注释和空白行
def is_valid_rule(line):
    line = line.strip()  # 去除首尾的空白字符
    # 检查是否为空行或以特殊字符开头（表示注释或非规则行）
    if not line or line.startswith(('!', '#', '[', ';', '//', '/*', '*/')):
        return False
    return True

# 判断是否为IP和域名映射规则
def is_ip_domain_mapping(line):
    return re.match(r'^\d{1,3}(\.\d{1,3}){3}\s+\S+', line) is not None

# 判断是否为纯IP地址
def is_ip_address(line):
    return re.match(r'^\d{1,3}(\.\d{1,3}){3}$', line) is not None

# 处理每一行规则，转换为统一格式
def process_line(line):
    line = line.strip()
    
    # 忽略IP和域名映射规则
    if is_ip_domain_mapping(line):
        return None
    
    # 如果是纯IP地址，则返回特定格式的规则
    if is_ip_address(line):
        return f"||{line}^"
    
    # 处理Host文件的规则，仅转换以0.0.0.0或127.0.0.1开头的行
    if line.startswith('0.0.0.0') or line.startswith('127.0.0.1'):
        parts = line.split()
        if len(parts) >= 2:  # 确保行中包含IP地址和域名
            domain = parts[1]
            return f"||{domain}^"
    
    # 处理Dnsmasq规则，只处理将域名定向到127.0.0.1或0.0.0.0的情况
    # 处理 address= 的情况
    if line.startswith('address='):
        parts = line.split('=')
        if len(parts) == 3:
            domain = parts[1]
            target_ip = parts[2]
            if target_ip == '127.0.0.1' or target_ip == '0.0.0.0':
                return f"||{domain}^"

    # 处理 server= 的情况
    elif line.startswith('server='):
        parts = line.split('=', 1)
        if len(parts) == 2:
            server_info = parts[1].split('/')
            if len(server_info) == 3:
                domain = server_info[1]
                target_ip = server_info[2]
                if target_ip == '127.0.0.1' or target_ip == '0.0.0.0':
                    return f"||{domain}^"
    
    # 忽略其他未处理的规则，返回原规则
    return line

# 异步下载过滤器规则
async def download_filter(session, url, retries=5):
    rules = set()  # 存储下载的规则
    attempt = 0
    # 重试机制
    while attempt < retries:
        try:
            async with session.get(url, ssl=False) as response:
                logging.info(f"Downloading from {url}, attempt {attempt + 1}")
                # 如果成功响应
                if response.status == 200:
                    logging.info(f"Successfully downloaded from {url}")
                    text = await response.text()
                    lines = text.splitlines()  # 分割每一行
                    # 处理每一行规则
                    for line in lines:
                        line = line.strip()
                        if is_valid_rule(line):  # 验证是否是有效规则
                            processed_line = process_line(line)  # 处理规则
                            if processed_line is not None:  # 忽略None值
                                rules.add(processed_line)  # 添加到规则集合
                    break
                else:
                    logging.error(f"Failed to download from {url} with status code {response.status}")
        except Exception as e:
            logging.error(f"Error downloading {url}: {e}")
        attempt += 1
        # 若重试次数未到最大，指数增加等待时间
        if attempt < retries:
            wait_time = 2 ** attempt  # 指数回退时间
            logging.info(f"Retrying in {wait_time} seconds...")
            await asyncio.sleep(wait_time)
        else:
            logging.error(f"Max retries reached for {url}")
    return rules

# 异步下载多个过滤器规则
async def download_filters(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [download_filter(session, url) for url in urls]  # 为每个URL创建任务
        all_rules = set()
        # 等待所有任务完成
        for future in asyncio.as_completed(tasks):
            rules = await future
            all_rules.update(rules)
    return all_rules

# 验证规则的有效性，移除无效规则
def validate_rules(rules):
    validated_rules = set()
    for rule in rules:
        if is_valid_rule(rule):
            validated_rules.add(rule)
    return validated_rules

# 将规则写入文件，并在文件头添加信息
def write_rules_to_file(rules, save_path):
    # 获取当前时间并设置为东八区时间
    now = datetime.now(timezone(timedelta(hours=8)))
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S %Z')  # 格式化时间戳

    # 文件头部注释信息
    header = f"""
!Title: Adblock-Rule-Collection
!Description: 一个汇总了多个广告过滤器过滤规则的广告过滤器订阅，每20分钟更新一次，确保即时同步上游减少误杀
!Homepage: https://github.com/REIJI007/Adblock-Rule-Collection
!LICENSE1: https://github.com/REIJI007/Adblock-Rule-Collection/blob/main/LICENSE-GPL 3.0
!LICENSE2: https://github.com/REIJI007/Adblock-Rule-Collection/blob/main/LICENSE-CC-BY-NC-SA 4.0
!生成时间: {timestamp}
!有效规则数目: {len(rules)}
"""
    # 将规则写入文件
    with open(save_path, 'w', encoding='utf-8') as f:
        logging.info(f"Writing {len(rules)} rules to file {save_path}")
        f.write(header)
        f.write('\n')
        # 过滤掉None值，确保只写入有效的规则
        f.writelines(f"{rule}\n" for rule in sorted(rules) if rule is not None)
    logging.info(f"Successfully wrote rules to {save_path}")
    print(f"Successfully wrote rules to {save_path}")
    print(f"有效规则数目: {len(rules)}")

# 主函数，负责执行流程
def main():
    logging.info("Starting to download filters...")
    print("Starting to download filters...")

    # 过滤器URL列表
    filter_urls = [
"https://anti-ad.net/adguard.txt",
#"https://raw.githubusercontent.com/Shura23/adghRuleShura23/refs/heads/v2/rule/easylist.txt",
"https://anti-ad.net/easylist.txt",
"https://small.oisd.nl",
"https://big.oisd.nl",
"https://easylist.to/easylist/easylist.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_adservers.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_thirdparty.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_adservers_popup.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_thirdparty_popup.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_allowlist.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_allowlist_dimensions.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_allowlist_general_hide.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_allowlist_popup.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_general_block.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_general_block_popup.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_general_hide.txt",
"https://easylist.to/easylist/easyprivacy.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_allowlist.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_allowlist_international.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_general.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_general_emailtrackers.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_thirdparty.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_thirdparty_international.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_trackingservers.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_trackingservers_thirdparty.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_trackingservers_admiral.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_trackingservers_general.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_trackingservers_mining.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_trackingservers_notifications.txt",
"https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easylist_cookie/easylist_cookie_allowlist.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easylist_cookie/easylist_cookie_allowlist_general_hide.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easylist_cookie/easylist_cookie_general_block.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easylist_cookie/easylist_cookie_general_hide.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easylist_cookie/easylist_cookie_thirdparty.txt",
"https://raw.githubusercontent.com/easylist/easylistchina/master/easylistchina.txt",
"https://easylist-downloads.adblockplus.org/antiadblockfilters.txt",
"https://secure.fanboy.co.nz/fanboy-annoyance.txt",
"https://easylist.to/easylist/fanboy-social.txt",
"https://www.fanboy.co.nz/fanboy-antifonts.txt",
"https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Other%20domains%20versions/FanboyNotifications-LoadableInUBO.txt",
"https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjx-annoyance.txt",
"https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjxlist.txt",
"https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjx-ublock.txt",
"https://raw.githubusercontent.com/uniartisan/adblock_list/master/adblock_plus.txt",
"https://raw.githubusercontent.com/uniartisan/adblock_list/master/adblock_privacy.txt",
"https://raw.githubusercontent.com/Cats-Team/AdRules/main/adblock_plus.txt",
"https://raw.githubusercontent.com/Cats-Team/AdRules/main/dns.txt",
"https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblockdns.txt",
"https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblockfilters.txt",
"https://raw.githubusercontent.com/8680/GOODBYEADS/master/data/rules/adblock.txt",
"https://raw.githubusercontent.com/8680/GOODBYEADS/master/data/rules/dns.txt",
"https://raw.githubusercontent.com/8680/GOODBYEADS/master/data/rules/allow.txt",
"https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-mobile.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances-cookies.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances-others.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/lan-block.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_2_Base/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_3_Spyware/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_4_Social/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_11_Mobile/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_14_Annoyances/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_15_DnsFilter/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_17_TrackParam/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_18_Annoyances_Cookies/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_19_Annoyances_Popups/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_20_Annoyances_MobileApp/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_21_Annoyances_Other/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_22_Annoyances_Widgets/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_224_Chinese/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_101_EasyList/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_104_EasyListChina/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_118_EasyPrivacy/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_122_FanboysAnnoyances/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_123_FanboysSocialBlockingList/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_201_WebAnnoyancesUltralist/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_204_PeterLowesList/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_207_AdblockWarningRemovalList/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_208_Online_Malicious_URL_Blocklist/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_209_ADgkMobileChinalist/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_210_Spam404/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_211_AntiAdblockKillerReek/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_219_ChinaListAndEasyList/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_220_CJXsAnnoyanceList/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_228_xinggsf/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_229_IdontCareAboutCookies/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_239_FanboyAntifonts/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_240_BarbBlock/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_241_FanboyCookiemonster/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_242_NoCoin/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_250_DandelionSproutAnnoyances/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_251_LegitimateURLShortener/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_255_Phishing_URL_Blocklist/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_256_Scam_Blocklist/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_257_uBlock_Origin_Badware_risks/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/BaseFilter/sections/adservers_firstparty.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/BaseFilter/sections/foreign.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/BaseFilter/sections/cryptominers.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/BaseFilter/sections/adservers.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/BaseFilter/sections/adservers_firstparty.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/BaseFilter/sections/allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/BaseFilter/sections/allowlist_stealth.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/BaseFilter/sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/BaseFilter/sections/replace.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/BaseFilter/sections/content_blocker.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardSDNSFilter/master/Filters/exclusions.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardSDNSFilter/master/Filters/exceptions.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardSDNSFilter/master/Filters/rules.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SpywareFilter/sections/tracking_servers_firstparty.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SpywareFilter/sections/tracking_servers.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SpywareFilter/sections/mobile.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SocialFilter/sections/allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SocialFilter/sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SocialFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SocialFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SocialFilter/sections/popups.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SocialFilter/sections/social_trackers.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/Cookies/sections/cookies_allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/Cookies/sections/cookies_general.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/MobileApp/sections/mobile-app_allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/MobileApp/sections/mobile-app_general.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/Popups/sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/Popups/sections/popups_allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/Popups/sections/popups_general.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/Popups/sections/push-notifications_allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/Popups/sections/push-notifications_general.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/Popups/sections/subscriptions_allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/Popups/sections/subscriptions_general.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/Widgets/sections/widgets.txt",
"https://raw.githubusercontent.com/AdguardTeam/cname-trackers/master/data/combined_original_trackers.txt",
"https://raw.githubusercontent.com/AdguardTeam/cname-trackers/master/data/combined_disguised_ads.txt",
"https://raw.githubusercontent.com/AdguardTeam/cname-trackers/master/data/combined_disguised_clickthroughs.txt",
"https://raw.githubusercontent.com/AdguardTeam/cname-trackers/master/data/combined_disguised_microsites.txt",
"https://raw.githubusercontent.com/AdguardTeam/cname-trackers/master/data/combined_disguised_trackers.txt",
"https://raw.githubusercontent.com/AdguardTeam/cname-trackers/master/data/combined_disguised_mail_trackers.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/ChineseFilter/sections/adservers.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/ChineseFilter/sections/adservers_firstparty.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/ChineseFilter/sections/allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/ChineseFilter/sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/ChineseFilter/sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/ChineseFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/ChineseFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/ChineseFilter/sections/replace.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/MobileFilter/sections/adservers.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/MobileFilter/sections/allowlist_app.txt",
"https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/MobileFilter/sections/allowlist_web.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/replace.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/cookies_allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/cookies_general.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/cookies_specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/mobile.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/mobile_allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/tracking_servers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/tracking_servers_firstparty.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/TrackParamFilter/sections/allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/TrackParamFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/Lynricsy/HyperADRules/master/rules.txt",
"https://raw.githubusercontent.com/Lynricsy/HyperADRules/master/dns.txt",
"https://raw.githubusercontent.com/Lynricsy/HyperADRules/master/allow.txt",
"https://raw.githubusercontent.com/xinggsf/Adblock-Plus-Rule/master/rule.txt",
"https://raw.githubusercontent.com/xinggsf/Adblock-Plus-Rule/master/mv.txt",
"https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/nocoin.txt",
"https://malware-filter.gitlab.io/malware-filter/phishing-filter-ag.txt",
"https://malware-filter.gitlab.io/malware-filter/phishing-filter-agh.txt",
"https://malware-filter.gitlab.io/malware-filter/phishing-filter.txt",
"https://malware-filter.gitlab.io/malware-filter/urlhaus-filter-ag.txt",
"https://malware-filter.gitlab.io/malware-filter/urlhaus-filter-agh.txt",
"https://malware-filter.gitlab.io/malware-filter/urlhaus-filter.txt",
"https://malware-filter.gitlab.io/malware-filter/tracking-filter.txt",
"https://malware-filter.gitlab.io/malware-filter/botnet-filter-ag.txt",
"https://malware-filter.gitlab.io/malware-filter/botnet-filter-agh.txt",
"https://malware-filter.gitlab.io/malware-filter/botnet-filter.txt",
"https://easylist-msie.adblockplus.org/abp-filters-anti-cv.txt",
"https://raw.githubusercontent.com/banbendalao/ADgk/master/ADgk.txt",
"https://raw.githubusercontent.com/yokoffing/filterlists/main/annoyance_list.txt",
"https://raw.githubusercontent.com/yokoffing/filterlists/main/privacy_essentials.txt",
"https://raw.githubusercontent.com/Spam404/lists/master/adblock-list.txt",
"https://raw.githubusercontent.com/brave/adblock-lists/master/brave-lists/brave-specific.txt",
"https://raw.githubusercontent.com/brave/adblock-lists/master/brave-lists/brave-ios-specific.txt",
"https://raw.githubusercontent.com/brave/adblock-lists/master/brave-lists/brave-android-specific.txt",
"https://raw.githubusercontent.com/brave/adblock-lists/master/brave-lists/brave-firstparty.txt",
"https://raw.githubusercontent.com/brave/adblock-lists/master/brave-lists/brave-firstparty-cname.txt",
"https://raw.githubusercontent.com/brave/adblock-lists/master/brave-unbreak.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_10_Useful/filter.txt",
"https://pgl.yoyo.org/adservers/serverlist.php?hostformat=adblockplus&showintro=0",
"https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareAdGuard.txt",
"https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareABP.txt",
"https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareAdGuardHome.txt",
"https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AdGuard%20Home%20Compilation%20List/AdGuardHomeCompilationList.txt",
"https://raw.githubusercontent.com/DandelionSprout/adfilt/master/LegitimateURLShortener.txt",
"https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/smart-tv-ags.txt",
"https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/ads-ags.txt",
"https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/basic-ags.txt",
"https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/tracking-ags.txt",
"https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/malware-ags.txt",
"https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/scam-ags.txt",
"https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/phishing-ags.txt",
"https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/ransomware-ags.txt",
"https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/fraud-ags.txt",
"https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/abuse-ags.txt",
"https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/redirect-ags.txt",
"https://raw.githubusercontent.com/reek/anti-adblock-killer/master/anti-adblock-killer-filters.txt",
"https://raw.githubusercontent.com/durablenapkin/scamblocklist/master/adguard.txt",
"https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV-AGH.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/pro.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/fake.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/light.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/dyndns.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/multi.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/personal.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/popupads.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/ultimate.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/spam-tlds-adblock-aggressive.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/spam-tlds-adblock-allow.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/tif.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/whitelist-referral.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/whitelist-urlshortener.txt",
"https://raw.githubusercontent.com/neodevpro/neodevhost/master/adblocker",
"https://raw.githubusercontent.com/damengzhu/banad/main/jiekouAD.txt",
"https://raw.githubusercontent.com/damengzhu/banad/main/dnslist.txt",
"https://hblock.molinero.dev/hosts_adblock.txt",
"https://raw.githubusercontent.com/badmojr/1Hosts/master/Pro/adblock.txt",
"https://filters.adavoid.org/ultimate-ad-filter.txt",
"https://filters.adavoid.org/ultimate-privacy-filter.txt",
"https://filters.adavoid.org/ultimate-security-filter.txt",
"https://filters.adtidy.org/extension/ublock/filters/2.txt",
"https://filters.adtidy.org/extension/ublock/filters/3.txt",
"https://filters.adtidy.org/extension/ublock/filters/4.txt",
"https://filters.adtidy.org/extension/ublock/filters/11.txt",
"https://filters.adtidy.org/extension/ublock/filters/14.txt",
"https://filters.adtidy.org/extension/ublock/filters/15.txt",
"https://filters.adtidy.org/extension/ublock/filters/17.txt",
"https://filters.adtidy.org/extension/ublock/filters/18.txt",
"https://filters.adtidy.org/extension/ublock/filters/19.txt",
"https://filters.adtidy.org/extension/ublock/filters/20.txt",
"https://filters.adtidy.org/extension/ublock/filters/21.txt",
"https://filters.adtidy.org/extension/ublock/filters/22.txt",
"https://filters.adtidy.org/extension/ublock/filters/101.txt",
"https://filters.adtidy.org/extension/ublock/filters/104.txt",
"https://filters.adtidy.org/extension/ublock/filters/118.txt",
"https://filters.adtidy.org/extension/ublock/filters/122.txt",
"https://filters.adtidy.org/extension/ublock/filters/123.txt",
"https://filters.adtidy.org/extension/ublock/filters/201.txt",
"https://filters.adtidy.org/extension/ublock/filters/204.txt",
"https://filters.adtidy.org/extension/ublock/filters/207.txt",
"https://filters.adtidy.org/extension/ublock/filters/208.txt",
"https://filters.adtidy.org/extension/ublock/filters/209.txt",
"https://filters.adtidy.org/extension/ublock/filters/220.txt",
"https://filters.adtidy.org/extension/ublock/filters/224.txt",
"https://filters.adtidy.org/extension/ublock/filters/228.txt",
"https://filters.adtidy.org/extension/ublock/filters/239.txt",
"https://filters.adtidy.org/extension/ublock/filters/240.txt",
"https://filters.adtidy.org/extension/ublock/filters/241.txt",
"https://filters.adtidy.org/extension/ublock/filters/242.txt",
"https://filters.adtidy.org/extension/ublock/filters/250.txt",
"https://filters.adtidy.org/extension/ublock/filters/251.txt",
"https://filters.adtidy.org/extension/ublock/filters/255.txt",
"https://filters.adtidy.org/extension/ublock/filters/256.txt",
"https://filters.adtidy.org/extension/ublock/filters/257.txt",
"https://filters.adtidy.org/extension/chromium/filters/2.txt",
"https://filters.adtidy.org/extension/chromium/filters/3.txt",
"https://filters.adtidy.org/extension/chromium/filters/4.txt",
"https://filters.adtidy.org/extension/chromium/filters/11.txt",
"https://filters.adtidy.org/extension/chromium/filters/14.txt",
"https://filters.adtidy.org/extension/chromium/filters/15.txt",
"https://filters.adtidy.org/extension/chromium/filters/17.txt",
"https://filters.adtidy.org/extension/chromium/filters/18.txt",
"https://filters.adtidy.org/extension/chromium/filters/19.txt",
"https://filters.adtidy.org/extension/chromium/filters/20.txt",
"https://filters.adtidy.org/extension/chromium/filters/21.txt",
"https://filters.adtidy.org/extension/chromium/filters/22.txt",
"https://filters.adtidy.org/extension/chromium/filters/101.txt",
"https://filters.adtidy.org/extension/chromium/filters/104.txt",
"https://filters.adtidy.org/extension/chromium/filters/118.txt",
"https://filters.adtidy.org/extension/chromium/filters/122.txt",
"https://filters.adtidy.org/extension/chromium/filters/123.txt",
"https://filters.adtidy.org/extension/chromium/filters/201.txt",
"https://filters.adtidy.org/extension/chromium/filters/204.txt",
"https://filters.adtidy.org/extension/chromium/filters/207.txt",
"https://filters.adtidy.org/extension/chromium/filters/208.txt",
"https://filters.adtidy.org/extension/chromium/filters/209.txt",
"https://filters.adtidy.org/extension/chromium/filters/220.txt",
"https://filters.adtidy.org/extension/chromium/filters/224.txt",
"https://filters.adtidy.org/extension/chromium/filters/228.txt",
"https://filters.adtidy.org/extension/chromium/filters/239.txt",
"https://filters.adtidy.org/extension/chromium/filters/240.txt",
"https://filters.adtidy.org/extension/chromium/filters/241.txt",
"https://filters.adtidy.org/extension/chromium/filters/242.txt",
"https://filters.adtidy.org/extension/chromium/filters/250.txt",
"https://filters.adtidy.org/extension/chromium/filters/251.txt",
"https://filters.adtidy.org/extension/chromium/filters/255.txt",
"https://filters.adtidy.org/extension/chromium/filters/256.txt",
"https://filters.adtidy.org/extension/chromium/filters/257.txt",
"https://filters.adtidy.org/extension/firefox/filters/2.txt",
"https://filters.adtidy.org/extension/firefox/filters/3.txt",
"https://filters.adtidy.org/extension/firefox/filters/4.txt",
"https://filters.adtidy.org/extension/firefox/filters/11.txt",
"https://filters.adtidy.org/extension/firefox/filters/14.txt",
"https://filters.adtidy.org/extension/firefox/filters/15.txt",
"https://filters.adtidy.org/extension/firefox/filters/17.txt",
"https://filters.adtidy.org/extension/firefox/filters/18.txt",
"https://filters.adtidy.org/extension/firefox/filters/19.txt",
"https://filters.adtidy.org/extension/firefox/filters/20.txt",
"https://filters.adtidy.org/extension/firefox/filters/21.txt",
"https://filters.adtidy.org/extension/firefox/filters/22.txt",
"https://filters.adtidy.org/extension/firefox/filters/101.txt",
"https://filters.adtidy.org/extension/firefox/filters/104.txt",
"https://filters.adtidy.org/extension/firefox/filters/118.txt",
"https://filters.adtidy.org/extension/firefox/filters/122.txt",
"https://filters.adtidy.org/extension/firefox/filters/123.txt",
"https://filters.adtidy.org/extension/firefox/filters/201.txt",
"https://filters.adtidy.org/extension/firefox/filters/204.txt",
"https://filters.adtidy.org/extension/firefox/filters/207.txt",
"https://filters.adtidy.org/extension/firefox/filters/208.txt",
"https://filters.adtidy.org/extension/firefox/filters/209.txt",
"https://filters.adtidy.org/extension/firefox/filters/220.txt",
"https://filters.adtidy.org/extension/firefox/filters/224.txt",
"https://filters.adtidy.org/extension/firefox/filters/228.txt",
"https://filters.adtidy.org/extension/firefox/filters/239.txt",
"https://filters.adtidy.org/extension/firefox/filters/240.txt",
"https://filters.adtidy.org/extension/firefox/filters/241.txt",
"https://filters.adtidy.org/extension/firefox/filters/242.txt",
"https://filters.adtidy.org/extension/firefox/filters/250.txt",
"https://filters.adtidy.org/extension/firefox/filters/251.txt",
"https://filters.adtidy.org/extension/firefox/filters/255.txt",
"https://filters.adtidy.org/extension/firefox/filters/256.txt",
"https://filters.adtidy.org/extension/firefox/filters/257.txt",
"https://filters.adtidy.org/windows/filters/2.txt",
"https://filters.adtidy.org/windows/filters/3.txt",
"https://filters.adtidy.org/windows/filters/4.txt",
"https://filters.adtidy.org/windows/filters/11.txt",
"https://filters.adtidy.org/windows/filters/14.txt",
"https://filters.adtidy.org/windows/filters/15.txt",
"https://filters.adtidy.org/windows/filters/17.txt",
"https://filters.adtidy.org/windows/filters/18.txt",
"https://filters.adtidy.org/windows/filters/19.txt",
"https://filters.adtidy.org/windows/filters/20.txt",
"https://filters.adtidy.org/windows/filters/21.txt",
"https://filters.adtidy.org/windows/filters/22.txt",
"https://filters.adtidy.org/windows/filters/101.txt",
"https://filters.adtidy.org/windows/filters/104.txt",
"https://filters.adtidy.org/windows/filters/118.txt",
"https://filters.adtidy.org/windows/filters/122.txt",
"https://filters.adtidy.org/windows/filters/123.txt",
"https://filters.adtidy.org/windows/filters/201.txt",
"https://filters.adtidy.org/windows/filters/204.txt",
"https://filters.adtidy.org/windows/filters/207.txt",
"https://filters.adtidy.org/windows/filters/208.txt",
"https://filters.adtidy.org/windows/filters/209.txt",
"https://filters.adtidy.org/windows/filters/220.txt",
"https://filters.adtidy.org/windows/filters/224.txt",
"https://filters.adtidy.org/windows/filters/228.txt",
"https://filters.adtidy.org/windows/filters/239.txt",
"https://filters.adtidy.org/windows/filters/240.txt",
"https://filters.adtidy.org/windows/filters/241.txt",
"https://filters.adtidy.org/windows/filters/242.txt",
"https://filters.adtidy.org/windows/filters/250.txt",
"https://filters.adtidy.org/windows/filters/251.txt",
"https://filters.adtidy.org/windows/filters/255.txt",
"https://filters.adtidy.org/windows/filters/256.txt",
"https://filters.adtidy.org/windows/filters/257.txt",
"https://filters.adtidy.org/android/filters/2_optimized.txt",
"https://filters.adtidy.org/android/filters/3_optimized.txt",
"https://filters.adtidy.org/android/filters/4_optimized.txt",
"https://filters.adtidy.org/android/filters/11_optimized.txt",
"https://filters.adtidy.org/android/filters/14_optimized.txt",
"https://filters.adtidy.org/android/filters/15_optimized.txt",
"https://filters.adtidy.org/android/filters/17_optimized.txt",
"https://filters.adtidy.org/android/filters/18_optimized.txt",
"https://filters.adtidy.org/android/filters/19_optimized.txt",
"https://filters.adtidy.org/android/filters/20_optimized.txt",
"https://filters.adtidy.org/android/filters/21_optimized.txt",
"https://filters.adtidy.org/android/filters/22_optimized.txt",
"https://filters.adtidy.org/android/filters/101_optimized.txt",
"https://filters.adtidy.org/android/filters/104_optimized.txt",
"https://filters.adtidy.org/android/filters/118_optimized.txt",
"https://filters.adtidy.org/android/filters/122_optimized.txt",
"https://filters.adtidy.org/android/filters/123_optimized.txt",
"https://filters.adtidy.org/android/filters/201_optimized.txt",
"https://filters.adtidy.org/android/filters/204_optimized.txt",
"https://filters.adtidy.org/android/filters/207_optimized.txt",
"https://filters.adtidy.org/android/filters/208_optimized.txt",
"https://filters.adtidy.org/android/filters/209_optimized.txt",
"https://filters.adtidy.org/android/filters/220_optimized.txt",
"https://filters.adtidy.org/android/filters/224_optimized.txt",
"https://filters.adtidy.org/android/filters/228_optimized.txt",
"https://filters.adtidy.org/android/filters/239_optimized.txt",
"https://filters.adtidy.org/android/filters/240_optimized.txt",
"https://filters.adtidy.org/android/filters/241_optimized.txt",
"https://filters.adtidy.org/android/filters/242_optimized.txt",
"https://filters.adtidy.org/android/filters/250_optimized.txt",
"https://filters.adtidy.org/android/filters/251_optimized.txt",
"https://filters.adtidy.org/android/filters/255_optimized.txt",
"https://filters.adtidy.org/android/filters/256_optimized.txt",
"https://filters.adtidy.org/android/filters/257_optimized.txt",
"https://filters.adtidy.org/ios/filters/2_optimized.txt",
"https://filters.adtidy.org/ios/filters/3_optimized.txt",
"https://filters.adtidy.org/ios/filters/4_optimized.txt",
"https://filters.adtidy.org/ios/filters/11_optimized.txt",
"https://filters.adtidy.org/ios/filters/14_optimized.txt",
"https://filters.adtidy.org/ios/filters/15_optimized.txt",
"https://filters.adtidy.org/ios/filters/17_optimized.txt",
"https://filters.adtidy.org/ios/filters/18_optimized.txt",
"https://filters.adtidy.org/ios/filters/19_optimized.txt",
"https://filters.adtidy.org/ios/filters/20_optimized.txt",
"https://filters.adtidy.org/ios/filters/21_optimized.txt",
"https://filters.adtidy.org/ios/filters/22_optimized.txt",
"https://filters.adtidy.org/ios/filters/101_optimized.txt",
"https://filters.adtidy.org/ios/filters/104_optimized.txt",
"https://filters.adtidy.org/ios/filters/118_optimized.txt",
"https://filters.adtidy.org/ios/filters/122_optimized.txt",
"https://filters.adtidy.org/ios/filters/123_optimized.txt",
"https://filters.adtidy.org/ios/filters/201_optimized.txt",
"https://filters.adtidy.org/ios/filters/204_optimized.txt",
"https://filters.adtidy.org/ios/filters/207_optimized.txt",
"https://filters.adtidy.org/ios/filters/208_optimized.txt",
"https://filters.adtidy.org/ios/filters/209_optimized.txt",
"https://filters.adtidy.org/ios/filters/220_optimized.txt",
"https://filters.adtidy.org/ios/filters/224_optimized.txt",
"https://filters.adtidy.org/ios/filters/228_optimized.txt",
"https://filters.adtidy.org/ios/filters/239_optimized.txt",
"https://filters.adtidy.org/ios/filters/240_optimized.txt",
"https://filters.adtidy.org/ios/filters/241_optimized.txt",
"https://filters.adtidy.org/ios/filters/242_optimized.txt",
"https://filters.adtidy.org/ios/filters/250_optimized.txt",
"https://filters.adtidy.org/ios/filters/251_optimized.txt",
"https://filters.adtidy.org/ios/filters/255_optimized.txt",
"https://filters.adtidy.org/ios/filters/256_optimized.txt",
"https://filters.adtidy.org/ios/filters/257_optimized.txt",
"https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Phishing-Angriffe",
"https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/malware",
"https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/spam.mails",
"https://adaway.org/hosts.txt",
"https://raw.githubusercontent.com/StevenBlack/hosts/master/data/StevenBlack/hosts"
    ]

    # 设置保存文件路径
    save_path = os.path.join(os.getcwd(), 'ADBLOCK_RULE_COLLECTION.txt')
    
    # 异步下载并处理过滤器规则
    rules = asyncio.run(download_filters(filter_urls))

    # 验证规则有效性
    validated_rules = validate_rules(rules)

    # 将规则写入文件
    write_rules_to_file(validated_rules, save_path)

# 如果脚本直接运行，调用main函数
if __name__ == '__main__':
    main()
    # 判断是否为交互模式
    if sys.stdin.isatty():
        input("Press Enter to exit...")
    else:
        print("Non-interactive mode, exiting...")
