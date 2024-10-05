[![GPL 3.0 license](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://github.com/REIJI007/Adblock-Rule-Collection/blob/main/LICENSE-GPL3.0)
[![CC BY-NC-SA 4.0 license](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://github.com/REIJI007/Adblock-Rule-Collection/blob/main/LICENSE-CC-BY-NC-SA%204.0)
<!-- 居中的大标题 -->
<h1 align="center" style="font-size: 100px; margin-bottom: 40px;">Adblock-Rule-Collection</h1>

<!-- 居中的副标题 -->
<h2 align="center" style="font-size: 30px; margin-bottom: 40px;">一个将众多广告过滤器条目转化、去重、合并汇总生成的广告拦截器和DNS过滤器，规则总数多达百万，包含URL过滤规则、资源过滤规则、域名过滤规则、CSS选择器过滤规则、脚本过滤规则、隐私保护规则、Cookie过滤规则、白名单例外规则、关键字过滤规则、webrtc拦截规则、正则表达式过滤规则、网络过滤规则、字体和样式过滤规则、重定向拦截规则、脚本注入规则、反指纹跟踪规则、欺诈过滤规则、恶意网站过滤规则、网络钓鱼过滤规则、滥用网站过滤规则、挖矿过滤规则、垃圾邮件过滤规则、僵尸网络屏蔽规则、地理位置追踪屏蔽规则、视音频广告过滤规则、社交媒体插件过滤规则、点击劫持保护规则、弹窗过滤规则等类型的条目</h2>

<!-- 徽章（根据需要调整） -->
<p align="center" style="margin-bottom: 40px;">
    <img src="https://img.shields.io/badge/last%20commit-today-brightgreen" alt="last commit" style="margin-right: 10px;">
    <img src="https://img.shields.io/github/forks/REIJI007/Adblock-Rule-Collection" alt="forks" style="margin-right: 10px;">
    <img src="https://img.shields.io/github/stars/REIJI007/Adblock-Rule-Collection" alt="stars" style="margin-right: 10px;">
    <img src="https://img.shields.io/github/issues/REIJI007/Adblock-Rule-Collection" alt="issues" style="margin-right: 10px;">
    <img src="https://img.shields.io/github/license/REIJI007/Adblock-Rule-Collection" alt="license" style="margin-right: 10px;">
</p>


## 一、关于Adblock-Rule-Collection，你可使用本仓库中的python脚本合并去重生成广告过滤规则列表，注意修改生成文件的保存路径与生成的文件名，可按需求添加不同的上游广告过滤规则列表（兼容adblock plus语法的过滤器列表均可）进行DIY定制，这个脚本也可以把host拦截规则和Dnsmasq拦截规则处理为adblock plus拦截规则，随着加入合并的广告过滤规则越来越多，生成文件体积也会越来越大，若你的广告过滤程序订阅失败则就下载规则文件充当本地用户过滤器。

<hr>

## 警告:本过滤器订阅有可能破坏某些网站的功能，也有可能封禁某些色情、赌博网站，使用前请斟酌考虑，如有误杀请积极向上游issue反馈，本仓库仅提供去重、转化、合并功能

<hr>
<br>

## 二、本仓库使用方式如下：

<hr> 
1、订阅地址

*广告过滤器*
<table border="1" style="border-collapse: collapse; width: 100%;">
  <tr>
    <th>版本</th>
    <th>链接</th>
  </tr>
  <tr>
    <td>完整版</td>
    <td>
      <strong><a href="https://raw.githubusercontent.com/REIJI007/Adblock-Rule-Collection/main/ADBLOCK_RULE_COLLECTION.txt">Github原始链接</a></strong> | 
      <strong><a href="https://adblock.reiji007.org/">Cloudflare加速链接</a></strong>
    </td>
  </tr>
  <tr>
    <td>精简版</td>
    <td>
      <strong><a href="https://raw.githubusercontent.com/REIJI007/Adblock-Rule-Collection/main/ADBLOCK_RULE_COLLECTION_Lite.txt">Github原始链接</a></strong> | 
      <strong><a href="https://adblock-lite.reiji007.org/">Cloudflare加速链接</a></strong>
    </td>
  </tr>
</table>

<br>

*DNS过滤器*
<table border="1" style="border-collapse: collapse; width: 100%;">
  <tr>
    <th>版本</th>
    <th>链接</th>
  </tr>
  <tr>
    <td>完整版</td>
    <td>
      <strong><a href="https://raw.githubusercontent.com/REIJI007/Adblock-Rule-Collection/main/ADBLOCK_RULE_COLLECTION_DNS.txt">Github原始链接</a></strong> | 
      <strong><a href="https://adblock-dns.reiji007.org/">Cloudflare加速链接</a></strong>
    </td>
  </tr>
  <tr>
    <td>精简版</td>
    <td>
      <strong><a href="https://raw.githubusercontent.com/REIJI007/Adblock-Rule-Collection/main/ADBLOCK_RULE_COLLECTION_DNS_Lite.txt">Github原始链接</a></strong> | 
      <strong><a href="https://adblock-dns-lite.reiji007.org/">Cloudflare加速链接</a></strong>
    </td>
  </tr>
</table>

<br>

*Host列表*
<table border="1" style="border-collapse: collapse; width: 100%;">
  <tr>
    <th>版本</th>
    <th>链接</th>
  </tr>
  <tr>
    <td>完整版</td>
    <td>
      <strong><a href="https://raw.githubusercontent.com/REIJI007/Adblock-Rule-Collection/main/ADBLOCK_RULE_COLLECTION_HOST.txt">Github原始链接</a></strong> | 
      <strong><a href="https://adblock-host.reiji007.org/">Cloudflare加速链接</a></strong>
    </td>
  </tr>
  <tr>
    <td>精简版</td>
    <td>
      <strong><a href="https://raw.githubusercontent.com/REIJI007/Adblock-Rule-Collection/main/ADBLOCK_RULE_COLLECTION_HOST_Lite.txt">Github原始链接</a></strong> | 
      <strong><a href="https://adblock-host-lite.reiji007.org/">Cloudflare加速链接</a></strong>
    </td>
  </tr>
</table>

<br>

2、从Release中下载过滤器文件进行本地导入过滤器，release每20分钟自动发布一次
<hr>


## 三、适用范围
适用于ADguard,Adblock Plus,uBlock Origin,Brave Browser等各类符合Adblock Plus 语法、uBlock Origin 语法、AdGuard 语法的浏览器插件或广告拦截程序以及DNS服务器
<br>


## 四、汇总引用规则列表有如下
<details>
  <summary>规则列表</summary>


1. [Anti-ad for ADguard](https://anti-ad.net/adguard.txt)  
2. [Anti-ad-Easylist](https://anti-ad.net/easylist.txt)
3. [OISD Small List](https://small.oisd.nl)
4. [OISD Big List](https://big.oisd.nl)  
5. [EasyList](https://easylist.to/easylist/easylist.txt)  
6. [EasyList-adservers](https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_adservers.txt)  
7. [EasyList-thirdparty_servers](https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_thirdparty.txt)  
8. [EasyList-adservers_popup](https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_adservers_popup.txt)  
9. [EasyList-thirdparty_popup](https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_thirdparty_popup.txt)  
10. [EasyList-allowlist](https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_allowlist.txt)  
11. [EasyList-allowlist_dimensions](https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_allowlist_dimensions.txt)  
12. [EasyList-allowlist_general_hide](https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_allowlist_general_hide.txt)  
13. [EasyList-allowlist_popup](https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_allowlist_popup.txt)  
14. [Easylist-general_block](https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_general_block.txt)  
15. [Easylist-general_block_popup](https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_general_block_popup.txt)  
16. [Easylist-general_hide](https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_general_hide.txt)  
17. [EasyPrivacy](https://easylist.to/easylist/easyprivacy.txt)  
18. [EasyPrivacy-allowlist](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_allowlist.txt)  
19. [EasyPrivacy-allowlist_international](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_allowlist_international.txt)  
20. [EasyPrivacy-general](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_general.txt)  
21. [EasyPrivacy-general_emailtrackers](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_general_emailtrackers.txt)  
22. [EasyPrivacy-third-party](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_thirdparty.txt)  
23. [EasyPrivacy-third-party international](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_thirdparty_international.txt)  
24. [EasyPrivacy-trackingservers](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_trackingservers.txt)  
25. [EasyPrivacy-trackingservers_thirdparty](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_trackingservers_thirdparty.txt)  
26. [EasyPrivacy-trackingservers_admiral](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_trackingservers_admiral.txt)  
27. [EasyPrivacy-trackingservers_general](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_trackingservers_general.txt)  
28. [EasyPrivacy-trackingservers_mining](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_trackingservers_mining.txt)  
29. [EasyPrivacy-trackingservers_notifications](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_trackingservers_notifications.txt)  
30. [Easylist Cookie List](https://secure.fanboy.co.nz/fanboy-cookiemonster.txt)  
31. [Easylist Cookie-allowlist](https://raw.githubusercontent.com/easylist/easylist/master/easylist_cookie/easylist_cookie_allowlist.txt)  
32. [Easylist Cookie-allowlist_general_hide](https://raw.githubusercontent.com/easylist/easylist/master/easylist_cookie/easylist_cookie_allowlist_general_hide.txt)  
33. [Easylist Cookie-general_block](https://raw.githubusercontent.com/easylist/easylist/master/easylist_cookie/easylist_cookie_general_block.txt)  
34. [Easylist Cookie-general_hide](https://raw.githubusercontent.com/easylist/easylist/master/easylist_cookie/easylist_cookie_general_hide.txt)  
35. [Easylist Cookie-thirdparty](https://raw.githubusercontent.com/easylist/easylist/master/easylist_cookie/easylist_cookie_thirdparty.txt)  
36. [EasyList China](https://raw.githubusercontent.com/easylist/easylistchina/master/easylistchina.txt)  
37. [Adblock Warning Removal List](https://easylist-downloads.adblockplus.org/antiadblockfilters.txt)  
38. [Fanboy's Annoyance List](https://secure.fanboy.co.nz/fanboy-annoyance.txt)  
39. [Fanboy's Social Blocking List](https://easylist.to/easylist/fanboy-social.txt)  
40. [Fanboy's Anti-thirdparty Fonts](https://www.fanboy.co.nz/fanboy-antifonts.txt)  
41. [Fanboy's Notifications Blocking List](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Other%20domains%20versions/FanboyNotifications-LoadableInUBO.txt)  
42. [CJX's Annoyance List](https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjx-annoyance.txt)  
43. [CJX's EasyList Lite](https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjxlist.txt)  
44. [CJX's uBlock list](https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjx-ublock.txt)  
45. [uniartrisan's Adblock List Plus](https://raw.githubusercontent.com/uniartisan/adblock_list/master/adblock_plus.txt)  
46. [uniartrisan's Privacy List](https://raw.githubusercontent.com/uniartisan/adblock_list/master/adblock_privacy.txt)  
47. [AdRules AdBlock List Plus](https://raw.githubusercontent.com/Cats-Team/AdRules/main/adblock_plus.txt)  
48. [AdRules DNS List](https://raw.githubusercontent.com/Cats-Team/AdRules/main/dns.txt)  
49. [AdBlock DNS](https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblockdns.txt)  
50. [AdBlock Filter](https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblockfilters.txt)  
51. [GOODBYEADS](https://raw.githubusercontent.com/8680/GOODBYEADS/master/data/rules/adblock.txt)
52. [GOODBYEADS-DNS](https://raw.githubusercontent.com/8680/GOODBYEADS/master/data/rules/dns.txt)  
53. [GOODBYEADS-allow](https://raw.githubusercontent.com/8680/GOODBYEADS/master/data/rules/allow.txt)  
54. [AWAvenue-Ads-Rule](https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt)  
55. [uBlock filters](https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt)  
56. [uBlock privacy filter](https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt)  
57. [uBlock mobile filter](https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-mobile.txt)  
58. [uBlock Badware risks filter](https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt)  
59. [uBlock Annoyances-Cookies filter](https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances-cookies.txt)  
60. [uBlock Annoyances-others filter](https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances-others.txt)  
61. [uBlock Resource abuse filters](https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt)  
62. [uBlock Unbreak filter](https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt)
63. [uBlock lan-block](https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/lan-block.txt)
64. [ADguard Base filter](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/filter_2_Base/filter.txt)  
65. [ADguard Spyware filter](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/filter_3_Spyware/filter.txt)  
66. [ADguard Social filter](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/filter_4_Social/filter.txt)  
67. [ADguard Mobile filter](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/filter_11_Mobile/filter.txt)  
68. [ADguard Annoyances filter](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/filter_14_Annoyances/filter.txt)  
69. [ADguard DnsFilter](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/filter_15_DnsFilter/filter.txt)  
70. [ADguard TrackParam filter](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/filter_17_TrackParam/filter.txt)  
71. [ADguard Annoyances_Cookies filter](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/filter_18_Annoyances_Cookies/filter.txt)  
72. [ADguard Annoyances_Popups filter](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/filter_19_Annoyances_Popups/filter.txt)  
73. [ADguard Annoyances_MobileApp filter](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/filter_20_Annoyances_MobileApp/filter.txt)  
74. [ADguard Annoyances_Other filter](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/filter_21_Annoyances_Other/filter.txt)  
75. [ADguard Annoyances_Widgets filter](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/filter_22_Annoyances_Widgets/filter.txt)  
76. [ADguard Chinese filter](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/filter_224_Chinese/filter.txt)  
77. [ADguard ThirdParty EasyList](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_101_EasyList/filter.txt)  
78. [ADguard ThirdParty EasyListChina](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_104_EasyListChina/filter.txt)  
79. [ADguard ThirdParty EasyPrivacy](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_118_EasyPrivacy/filter.txt)  
80. [ADguard ThirdParty Fanboy's Annoyance List](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_122_FanboysAnnoyances/filter.txt)  
81. [ADguard ThirdParty FanboysSocialBlockingList](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_123_FanboysSocialBlockingList/filter.txt)  
82. [ADguard ThirdParty WebAnnoyancesUltralist](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_201_WebAnnoyancesUltralist/filter.txt)  
83. [ADguard ThirdParty PeterLowesList](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_204_PeterLowesList/filter.txt)  
84. [ADguard ThirdParty AdblockWarningRemovalList](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_207_AdblockWarningRemovalList/filter.txt)  
85. [ADguard ThirdParty Online_Malicious_URL_Blocklist](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_208_Online_Malicious_URL_Blocklist/filter.txt)  
86. [ADguard ThirdParty ADgkMobileChinalist](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_209_ADgkMobileChinalist/filter.txt)  
87. [ADguard ThirdParty Spam404](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_210_Spam404/filter.txt)  
88. [ADguard ThirdParty Anti-Adblock Killer](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_211_AntiAdblockKillerReek/filter.txt)  
89. [ADguard ThirdParty ChinaListAndEasyList](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_219_ChinaListAndEasyList/filter.txt)  
90. [ADguard ThirdParty CJXsAnnoyanceList](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_220_CJXsAnnoyanceList/filter.txt)  
91. [ADguard ThirdParty xinggsf](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_228_xinggsf/filter.txt)  
92. [ADguard ThirdParty IdontCareAboutCookies](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_229_IdontCareAboutCookies/filter.txt)  
93. [ADguard ThirdParty FanboyAntifonts](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_239_FanboyAntifonts/filter.txt)  
94. [ADguard ThirdParty BarbBlock](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_240_BarbBlock/filter.txt)  
95. [ADguard ThirdParty FanboyCookiemonster](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_241_FanboyCookiemonster/filter.txt)  
96. [ADguard ThirdParty NoCoin](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_242_NoCoin/filter.txt)  
97. [ADguard ThirdParty DandelionSproutAnnoyances](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_250_DandelionSproutAnnoyances/filter.txt)  
98. [ADguard ThirdParty Legitimate_URL_Shortener](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_251_LegitimateURLShortener/filter.txt)  
99. [ADguard ThirdParty Phishing_URL_Blocklist](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_255_Phishing_URL_Blocklist/filter.txt)  
100. [ADguard ThirdParty Scam_Blocklist](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_256_Scam_Blocklist/filter.txt)  
101. [ADguard ThirdParty uBlock_Origin_Badware_risks](https://raw.githubusercontent.com/ADguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_257_uBlock_Origin_Badware_risks/filter.txt)  
102. [ADguard Base filter-first-party servers](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/BaseFilter/sections/adservers_firstparty.txt)
103. [ADguard Base filter-foreign servers](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/BaseFilter/sections/foreign.txt)  
104. [ADguard Base filter cryptominers](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/BaseFilter/sections/cryptominers.txt)  
105. [ADguard Base filter-adservers](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/BaseFilter/sections/adservers.txt)  
106. [ADguard Base filter-adservers_firstparty](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/BaseFilter/sections/adservers_firstparty.txt)  
107. [ADguard Base filter-allowlist](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/BaseFilter/sections/allowlist.txt)  
108. [ADguard Base filter-allowlist_stealth](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/BaseFilter/sections/allowlist_stealth.txt)  
109. [ADguard Base filter-antiadblock](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/BaseFilter/sections/antiadblock.txt)  
110. [ADguard Base filter-replace](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/BaseFilter/sections/replace.txt)  
111. [ADguard Base filter-content_blocker](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/BaseFilter/sections/content_blocker.txt)  
112. [ADguard Exclusion rules](https://raw.githubusercontent.com/ADguardTeam/ADguardSDNSFilter/master/Filters/exclusions.txt)  
113. [ADguard Exception rules](https://raw.githubusercontent.com/ADguardTeam/ADguardSDNSFilter/master/Filters/exceptions.txt)  
114. [ADguardSDNSFilter](https://raw.githubusercontent.com/ADguardTeam/ADguardSDNSFilter/master/Filters/rules.txt)  
115. [ADguard Tracking Protection filter - first-party trackers](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/SpywareFilter/sections/tracking_servers_firstparty.txt)  
116. [ADguard Tracking Protection filter - third-party trackers](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/SpywareFilter/sections/tracking_servers.txt)  
117. [ADguard Tracking Protection filter - mobile trackers](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/SpywareFilter/sections/mobile.txt)  
118. [ADguard Social filter-allowlist](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/SocialFilter/sections/allowlist.txt)  
119. [ADguard Social filter-general_elemhide](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/SocialFilter/sections/general_elemhide.txt)  
120. [ADguard Social filter-general_extensions](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/SocialFilter/sections/general_extensions.txt)  
121. [ADguard Social filter-general_url](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/SocialFilter/sections/general_url.txt)  
122. [ADguard Social filter-popups](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/SocialFilter/sections/popups.txt)  
123. [ADguard Social filter-social_trackers](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/SocialFilter/sections/social_trackers.txt)  
124. [ADguard Annoyances filter-cookies_allowlist](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/AnnoyancesFilter/Cookies/sections/cookies_allowlist.txt)  
125. [ADguard Annoyances filter-cookies_general](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/AnnoyancesFilter/Cookies/sections/cookies_general.txt)  
126. [ADguard Annoyances filter-mobile-app_allowlist](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/AnnoyancesFilter/MobileApp/sections/mobile-app_allowlist.txt)  
127. [ADguard Annoyances filter-mobile-app_general](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/AnnoyancesFilter/MobileApp/sections/mobile-app_general.txt)  
128. [ADguard Annoyances filter-popups-antiadblock](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/AnnoyancesFilter/Popups/sections/antiadblock.txt)  
129. [ADguard Annoyances filter-popups-allowlist](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/AnnoyancesFilter/Popups/sections/popups_allowlist.txt)  
130. [ADguard Annoyances filter-popups-general](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/AnnoyancesFilter/Popups/sections/popups_general.txt)  
131. [ADguard Annoyances filter-popups-push-notifications_allowlist](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/AnnoyancesFilter/Popups/sections/push-notifications_allowlist.txt)  
132. [ADguard Annoyances filter-popups-push-notifications_general](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/AnnoyancesFilter/Popups/sections/push-notifications_general.txt)  
133. [ADguard Annoyances filter-popups-subscriptions_allowlist](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/AnnoyancesFilter/Popups/sections/subscriptions_allowlist.txt)  
134. [ADguard Annoyances filter-popups-subscriptions_general](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/AnnoyancesFilter/Popups/sections/subscriptions_general.txt)  
135. [ADguard Annoyances filter-Widgets](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/AnnoyancesFilter/Widgets/sections/widgets.txt)  
136. [ADguard CNAME original trackers list](https://raw.githubusercontent.com/ADguardTeam/cname-trackers/master/data/combined_original_trackers.txt)  
137. [ADguard CNAME disguised ads list](https://raw.githubusercontent.com/ADguardTeam/cname-trackers/master/data/combined_disguised_ads.txt)  
138. [ADguard CNAME disguised clickthroughs list](https://raw.githubusercontent.com/ADguardTeam/cname-trackers/master/data/combined_disguised_clickthroughs.txt)  
139. [ADguard CNAME disguised microsites list](https://raw.githubusercontent.com/ADguardTeam/cname-trackers/master/data/combined_disguised_microsites.txt)  
140. [ADguard CNAME disguised trackers list](https://raw.githubusercontent.com/ADguardTeam/cname-trackers/master/data/combined_disguised_trackers.txt)  
141. [ADguard CNAME disguised mail_trackers list](https://raw.githubusercontent.com/ADguardTeam/cname-trackers/master/data/combined_disguised_mail_trackers.txt)  
142. [ADguard Chinese filter-adservers](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/ChineseFilter/sections/adservers.txt)  
143. [ADguard Chinese filter-adservers_firstparty](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/ChineseFilter/sections/adservers_firstparty.txt)  
144. [ADguard ChineseFilter-allowlist](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/ChineseFilter/sections/allowlist.txt)  
145. [ADguard ChineseFilter-antiadblock](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/ChineseFilter/sections/antiadblock.txt)  
146. [ADguard ChineseFilter-general_elemhide](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/ChineseFilter/sections/general_elemhide.txt)  
147. [ADguard ChineseFilter-general_extensions](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/ChineseFilter/sections/general_extensions.txt)  
148. [ADguard ChineseFilter-general_url](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/ChineseFilter/sections/general_url.txt)  
149. [ADguard ChineseFilter-replace](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/ChineseFilter/sections/replace.txt)  
150. [ADguard Mobile filter-adservers](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/MobileFilter/sections/adservers.txt)  
151. [ADguard MobileFilter-allowlist_app](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/MobileFilter/sections/allowlist_app.txt)  
152. [ADguard MobileFilter-allowlist_web](https://raw.githubusercontent.com/ADguardTeam/ADguardFilters/master/MobileFilter/sections/allowlist_web.txt)  
153. [ADguard MobileFilter-antiadblock](https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/antiadblock.txt)  
154. [ADguard MobileFilter-general_elemhide](https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/general_elemhide.txt)  
155. [ADguard MobileFilter-general_extensions](https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/general_extensions.txt)  
156. [ADguard MobileFilter-general_url](https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/general_url.txt)  
157. [ADguard MobileFilter-replace](https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/replace.txt)  
158. [ADguard SpywareFilter-allowlist](https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/allowlist.txt)  
159. [ADguard SpywareFilter-cookies_allowlist](https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/cookies_allowlist.txt)  
160. [ADguard SpywareFilter-cookies_general](https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/cookies_general.txt)  
161. [ADguard SpywareFilter-cookies_specific](https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/cookies_specific.txt)  
162. [ADguard SpywareFilter-general_elemhide](https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/general_elemhide.txt)  
163. [ADguard SpywareFilter-general_extensions](https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/general_extensions.txt)  
164. [ADguard SpywareFilter-general_url](https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/general_url.txt)  
165. [ADguard SpywareFilter-mobile](https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/mobile.txt)  
166. [ADguard SpywareFilter-mobile_allowlist](https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/mobile_allowlist.txt)  
167. [ADguard SpywareFilter-tracking_servers](https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/tracking_servers.txt)  
168. [ADguard SpywareFilter-tracking_servers_firstparty](https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/tracking_servers_firstparty.txt)  
169. [ADguard TrackParamFilter-allowlist](https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/TrackParamFilter/sections/allowlist.txt)  
170. [ADguard TrackParamFilter-general_url](https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/TrackParamFilter/sections/general_url.txt)  
171. [HyperADRules](https://raw.githubusercontent.com/Lynricsy/HyperADRules/master/rules.txt)  
172. [HyperADRules-DNS](https://raw.githubusercontent.com/Lynricsy/HyperADRules/master/dns.txt)  
173. [HyperADRules-allow](https://raw.githubusercontent.com/Lynricsy/HyperADRules/master/allow.txt)  
174. [xinggsf's rules](https://raw.githubusercontent.com/xinggsf/Adblock-Plus-Rule/master/rule.txt)  
175. [xinggsf's mv rules](https://raw.githubusercontent.com/xinggsf/Adblock-Plus-Rule/master/mv.txt)  
176. [adblock-nocoin-list](https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/nocoin.txt)    
177. [Phishing URL Blocklist-AdGuard](https://malware-filter.gitlab.io/malware-filter/phishing-filter-ag.txt)  
178. [Phishing URL Blocklist-AdGuard Home](https://malware-filter.gitlab.io/malware-filter/phishing-filter-agh.txt)  
179. [Phishing URL Blocklist-uBlock Origin](https://malware-filter.gitlab.io/malware-filter/phishing-filter.txt)  
180. [Malicious URL Blocklist-AdGuard](https://malware-filter.gitlab.io/malware-filter/urlhaus-filter-ag.txt)  
181. [Malicious URL Blocklist-AdGuard Home](https://malware-filter.gitlab.io/malware-filter/urlhaus-filter-agh.txt)  
182. [Malicious URL Blocklist-uBlock Origin](https://malware-filter.gitlab.io/malware-filter/urlhaus-filter.txt)  
183. [Tracking JS Blocklist](https://malware-filter.gitlab.io/malware-filter/tracking-filter.txt)  
184. [Botnet IP Blocklist - AdGuard](https://malware-filter.gitlab.io/malware-filter/botnet-filter-ag.txt)  
185. [Botnet IP Blocklist - AdGuard Home](https://malware-filter.gitlab.io/malware-filter/botnet-filter-agh.txt)  
186. [Botnet IP Blocklist - uBlock Origin](https://malware-filter.gitlab.io/malware-filter/botnet-filter.txt)  
187. [ABP filters](https://easylist-msie.adblockplus.org/abp-filters-anti-cv.txt)  
188. [adgk](https://raw.githubusercontent.com/banbendalao/ADgk/master/ADgk.txt)  
189. [yokoffing's Annoyance List](https://raw.githubusercontent.com/yokoffing/filterlists/main/annoyance_list.txt)  
190. [yokoffing's Privacy Essentials](https://raw.githubusercontent.com/yokoffing/filterlists/main/privacy_essentials.txt)  
191. [Spam404's Adblock-list](https://raw.githubusercontent.com/Spam404/lists/master/adblock-list.txt)  
192. [Brave-specific filter](https://raw.githubusercontent.com/brave/adblock-lists/master/brave-lists/brave-specific.txt)  
193. [Brave-ios-specific filter](https://raw.githubusercontent.com/brave/adblock-lists/master/brave-lists/brave-ios-specific.txt)  
194. [Brave-Android-specific filter](https://raw.githubusercontent.com/brave/adblock-lists/master/brave-lists/brave-android-specific.txt)  
195. [Brave-Firstparty filter](https://raw.githubusercontent.com/brave/adblock-lists/master/brave-lists/brave-firstparty.txt)  
196. [Brave-Firstparty-cname filter](https://raw.githubusercontent.com/brave/adblock-lists/master/brave-lists/brave-firstparty-cname.txt)  
197. [Brave-Unbreak filter](https://raw.githubusercontent.com/brave/adblock-lists/master/brave-unbreak.txt)  
198. [Filter unblocking search ads and self-promotions](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_10_Useful/filter.txt)  
199. [Peter Lowe's Ad and Tracking Server List](https://pgl.yoyo.org/adservers/serverlist.php?hostformat=adblockplus&showintro=0)
200. [Dandelion Sprout's Anti-Malware List (for ADguard)](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareAdGuard.txt)
201. [Dandelion Sprout's Anti-Malware List (for Adblock Plus and AdBlock)](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareABP.txt)
202. [Dandelion Sprout's Compilation List](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AdGuard%20Home%20Compilation%20List/AdGuardHomeCompilationList.txt)
203. [Dandelion Sprout's Anti-Malware List (for AdGuardHome)](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareAdGuardHome.txt)
204. [Dandelion Sprout's Legitimate URL Shortener](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/LegitimateURLShortener.txt)
205. [The Block List Project - Smart TV List](https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/smart-tv-ags.txt)
206. [The Block List Project - Ads List](https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/ads-ags.txt)
207. [The Block List Project - Basic Starter List](https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/basic-ags.txt)
208. [The Block List Project - Tracking List](https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/tracking-ags.txt)
209. [The Block List Project - Malware List](https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/malware-ags.txt)
210. [The Block List Project - Scam List](https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/scam-ags.txt)
211. [The Block List Project - Phishing List](https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/phishing-ags.txt)
212. [The Block List Project - Ransomware List](https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/ransomware-ags.txt)
213. [The Block List Project - Fraud List](https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/fraud-ags.txt)
214. [The Block List Project - Abuse List](https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/abuse-ags.txt)
215. [The Block List Project - Redirect List](https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/redirect-ags.txt)
216. [Anti-Adblock Killer](https://raw.githubusercontent.com/reek/anti-adblock-killer/master/anti-adblock-killer-filters.txt)
217. [Scam Blocklist (Adblock Plus)](https://raw.githubusercontent.com/durablenapkin/scamblocklist/master/adguard.txt)
218. [Smart-TV Blocklist for ADguard Home](https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV-AGH.txt)
219. [HaGeZi's Pro DNS Blocklist](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/pro.txt)
220. [HaGeZi's Fake DNS Blocklist](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/fake.txt)
221. [HaGeZi's Light DNS Blocklist](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/light.txt)
222. [HaGeZi's DynDNS Blocklist](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/dyndns.txt)
223. [HaGeZi's Normal DNS Blocklist](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/multi.txt)
224. [HaGeZi's Personal DNS Blocklist](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/personal.txt)
225. [HaGeZi's Pop-Up Ads DNS Blocklist](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/popupads.txt)
226. [HaGeZi's Ultimate DNS Blocklist](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/ultimate.txt)
227. [HaGeZi's The World's Most Abused TLDs - Aggressive](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/spam-tlds-adblock-aggressive.txt)
228. [HaGeZi's The World's Most Abused TLDs - Allow](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/spam-tlds-adblock-allow.txt)
229. [HaGeZi's Threat Intelligence Feeds DNS Blocklist](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/tif.txt)
230. [HaGeZi's Allowlist Referral](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/whitelist-referral.txt)
231. [HaGeZi's Allowlist URL Shortener](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/whitelist-urlshortener.txt)
232. [neodevpro's adblock list](https://raw.githubusercontent.com/neodevpro/neodevhost/master/adblocker)
233. [damengzhu's adblock List](https://raw.githubusercontent.com/damengzhu/banad/main/jiekouAD.txt)
234. [damengzhu's DNS List](https://raw.githubusercontent.com/damengzhu/banad/main/dnslist.txt)
235. [hectorm's adblock List](https://hblock.molinero.dev/hosts_adblock.txt)
236. [1Hosts's adblock list](https://raw.githubusercontent.com/badmojr/1Hosts/master/Pro/adblock.txt)
237. [ADblocker Ultimate Ad Filter](https://filters.adavoid.org/ultimate-ad-filter.txt)
238. [ADblocker Ultimate Privacy Filter](https://filters.adavoid.org/ultimate-privacy-filter.txt)
239. [ADblocker Ultimate Security Filter](https://filters.adavoid.org/ultimate-security-filter.txt)
240. [ADguard Base filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/2.txt)
241. [ADguard Tracking Protection filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/3.txt)
242. [ADguard Social Media filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/4.txt)
243. [ADguard Mobile Ads filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/11.txt)
244. [ADguard Annoyances filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/14.txt)
245. [ADguard DNS filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/15.txt)
246. [ADguard URL Tracking filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/17.txt)
247. [ADguard Cookie Notices filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/18.txt)
248. [ADguard Popups filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/19.txt)
249. [ADguard Mobile App Banners filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/20.txt)  
250. [ADguard Other Annoyances filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/21.txt)  
251. [ADguard Widgets filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/22.txt)  
252. [Easylist (ublock)](https://filters.adtidy.org/extension/ublock/filters/101.txt)  
253. [Easylist China (ublock)](https://filters.adtidy.org/extension/ublock/filters/104.txt)  
254. [EasyPrivacy (ublock)](https://filters.adtidy.org/extension/ublock/filters/118.txt)  
255. [Fanboy's Annoyances (ublock)](https://filters.adtidy.org/extension/ublock/filters/122.txt)  
256. [Fanboy's Social Blocking List (ublock)](https://filters.adtidy.org/extension/ublock/filters/123.txt)  
257. [Web Annoyances Ultralist (ublock)](https://filters.adtidy.org/extension/ublock/filters/201.txt)  
258. [Peter Lowe's Blocklist (ublock)](https://filters.adtidy.org/extension/ublock/filters/204.txt)  
259. [Adblock Warning Removal List (ublock)](https://filters.adtidy.org/extension/ublock/filters/207.txt)  
260. [Online Malicious URL Blocklist (ublock)](https://filters.adtidy.org/extension/ublock/filters/208.txt)  
261. [ADgk Mobile China list (ublock)](https://filters.adtidy.org/extension/ublock/filters/209.txt)  
262. [CJX's Annoyances List (ublock)](https://filters.adtidy.org/extension/ublock/filters/220.txt)  
263. [ADguard Chinese filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/224.txt)  
264. [xinggsf (ublock)](https://filters.adtidy.org/extension/ublock/filters/228.txt)  
265. [Fanboy's Anti-thirdparty Fonts (ublock)](https://filters.adtidy.org/extension/ublock/filters/239.txt)  
266. [BarbBlock (ublock)](https://filters.adtidy.org/extension/ublock/filters/240.txt)  
267. [EasyList Cookie List (ublock)](https://filters.adtidy.org/extension/ublock/filters/241.txt)  
268. [NoCoin Filter List (ublock)](https://filters.adtidy.org/extension/ublock/filters/242.txt)  
269. [Dandelion Sprout's Annoyances List (ublock)](https://filters.adtidy.org/extension/ublock/filters/250.txt)  
270. [Legitimate URL Shortener (ublock)](https://filters.adtidy.org/extension/ublock/filters/251.txt)  
271. [Phishing URL Blocklist (ublock)](https://filters.adtidy.org/extension/ublock/filters/255.txt)  
272. [Scam Blocklist (ublock)](https://filters.adtidy.org/extension/ublock/filters/256.txt)  
273. [uBlock Origin - Badware risks (ublock)](https://filters.adtidy.org/extension/ublock/filters/257.txt)  
274. [ADguard Base filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/2.txt)  
275. [ADguard Tracking Protection filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/3.txt)  
276. [ADguard Social Media filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/4.txt)  
277. [ADguard Mobile Ads filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/11.txt)  
278. [ADguard Annoyances filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/14.txt)  
279. [ADguard DNS filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/15.txt)  
280. [ADguard URL Tracking filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/17.txt)  
281. [ADguard Cookie Notices filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/18.txt)  
282. [ADguard Popups filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/19.txt)  
283. [ADguard Mobile App Banners filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/20.txt)  
284. [ADguard Other Annoyances filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/21.txt)  
285. [ADguard Widgets filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/22.txt)  
286. [Easylist (chromium)](https://filters.adtidy.org/extension/chromium/filters/101.txt)  
287. [Easylist China (chromium)](https://filters.adtidy.org/extension/chromium/filters/104.txt)  
288. [EasyPrivacy (chromium)](https://filters.adtidy.org/extension/chromium/filters/118.txt)  
289. [Fanboy's Annoyances (chromium)](https://filters.adtidy.org/extension/chromium/filters/122.txt)  
290. [Fanboy's Social Blocking List (chromium)](https://filters.adtidy.org/extension/chromium/filters/123.txt)  
291. [Web Annoyances Ultralist (chromium)](https://filters.adtidy.org/extension/chromium/filters/201.txt)  
292. [Peter Lowe's Blocklist (chromium)](https://filters.adtidy.org/extension/chromium/filters/204.txt)  
293. [Adblock Warning Removal List (chromium)](https://filters.adtidy.org/extension/chromium/filters/207.txt)  
294. [Online Malicious URL Blocklist (chromium)](https://filters.adtidy.org/extension/chromium/filters/208.txt)  
295. [ADgk Mobile China list (chromium)](https://filters.adtidy.org/extension/chromium/filters/209.txt)  
296. [CJX's Annoyances List (chromium)](https://filters.adtidy.org/extension/chromium/filters/220.txt)  
297. [ADguard Chinese filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/224.txt)
298. [xinggsf (chromium)](https://filters.adtidy.org/extension/chromium/filters/228.txt)
299. [Fanboy's Anti-thirdparty Fonts (chromium)](https://filters.adtidy.org/extension/chromium/filters/239.txt)
300. [BarbBlock (chromium)](https://filters.adtidy.org/extension/chromium/filters/240.txt)
301. [EasyList Cookie List (chromium)](https://filters.adtidy.org/extension/chromium/filters/241.txt)
302. [NoCoin Filter List (chromium)](https://filters.adtidy.org/extension/chromium/filters/242.txt)
303. [Dandelion Sprout's Annoyances List (chromium)](https://filters.adtidy.org/extension/chromium/filters/250.txt)
304. [Legitimate URL Shortener (chromium)](https://filters.adtidy.org/extension/chromium/filters/251.txt)
305. [Phishing URL Blocklist (chromium)](https://filters.adtidy.org/extension/chromium/filters/255.txt)
306. [Scam Blocklist (chromium)](https://filters.adtidy.org/extension/chromium/filters/256.txt)
307. [uBlock Origin - Badware risks (chromium)](https://filters.adtidy.org/extension/chromium/filters/257.txt)
308. [ADguard Base filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/2.txt)
309. [ADguard Tracking Protection filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/3.txt)
310. [ADguard Social Media filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/4.txt)
311. [ADguard Mobile Ads filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/11.txt)
312. [ADguard Annoyances filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/14.txt)
313. [ADguard DNS filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/15.txt)
314. [ADguard URL Tracking filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/17.txt)
315. [ADguard Cookie Notices filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/18.txt)
316. [ADguard Popups filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/19.txt)
317. [ADguard Mobile App Banners filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/20.txt)
318. [ADguard Other Annoyances filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/21.txt)
319. [ADguard Widgets filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/22.txt)
320. [Easylist (firefox)](https://filters.adtidy.org/extension/firefox/filters/101.txt)
321. [Easylist China (firefox)](https://filters.adtidy.org/extension/firefox/filters/104.txt)
322. [EasyPrivacy (firefox)](https://filters.adtidy.org/extension/firefox/filters/118.txt)
323. [Fanboy's Annoyances (firefox)](https://filters.adtidy.org/extension/firefox/filters/122.txt)
324. [Fanboy's Social Blocking List (firefox)](https://filters.adtidy.org/extension/firefox/filters/123.txt)
325. [Web Annoyances Ultralist (firefox)](https://filters.adtidy.org/extension/firefox/filters/201.txt)
326. [Peter Lowe's Blocklist (firefox)](https://filters.adtidy.org/extension/firefox/filters/204.txt)
327. [Adblock Warning Removal List (firefox)](https://filters.adtidy.org/extension/firefox/filters/207.txt)
328. [Online Malicious URL Blocklist (firefox)](https://filters.adtidy.org/extension/firefox/filters/208.txt)
329. [ADgk Mobile China list (firefox)](https://filters.adtidy.org/extension/firefox/filters/209.txt)
330. [CJX's Annoyances List (firefox)](https://filters.adtidy.org/extension/firefox/filters/220.txt)
331. [ADguard Chinese filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/224.txt)
332. [xinggsf (firefox)](https://filters.adtidy.org/extension/firefox/filters/228.txt)
333. [Fanboy's Anti-thirdparty Fonts (firefox)](https://filters.adtidy.org/extension/firefox/filters/239.txt)
334. [BarbBlock (firefox)](https://filters.adtidy.org/extension/firefox/filters/240.txt)
335. [EasyList Cookie List (firefox)](https://filters.adtidy.org/extension/firefox/filters/241.txt)
336. [NoCoin Filter List (firefox)](https://filters.adtidy.org/extension/firefox/filters/242.txt)
337. [Dandelion Sprout's Annoyances List (firefox)](https://filters.adtidy.org/extension/firefox/filters/250.txt)
338. [Legitimate URL Shortener (firefox)](https://filters.adtidy.org/extension/firefox/filters/251.txt)
339. [Phishing URL Blocklist (firefox)](https://filters.adtidy.org/extension/firefox/filters/255.txt)
340. [Scam Blocklist (firefox)](https://filters.adtidy.org/extension/firefox/filters/256.txt)
341. [uBlock Origin - Badware risks (firefox)](https://filters.adtidy.org/extension/firefox/filters/257.txt)
342. [ADguard Base filter (windows)](https://filters.adtidy.org/windows/filters/2.txt)
343. [ADguard Tracking Protection filter (windows)](https://filters.adtidy.org/windows/filters/3.txt)
344. [ADguard Social Media filter (windows)](https://filters.adtidy.org/windows/filters/4.txt)  
345. [ADguard Mobile Ads filter (windows)](https://filters.adtidy.org/windows/filters/11.txt)
346. [ADguard Annoyances filter (windows)](https://filters.adtidy.org/windows/filters/14.txt)  
347. [ADguard DNS filter (windows)](https://filters.adtidy.org/windows/filters/15.txt)  
348. [ADguard URL Tracking filter (windows)](https://filters.adtidy.org/windows/filters/17.txt)  
349. [ADguard Cookie Notices filter (windows)](https://filters.adtidy.org/windows/filters/18.txt)  
350. [ADguard Popups filter (windows)](https://filters.adtidy.org/windows/filters/19.txt)  
351. [ADguard Mobile App Banners filter (windows)](https://filters.adtidy.org/windows/filters/20.txt)  
352. [ADguard Other Annoyances filter (windows)](https://filters.adtidy.org/windows/filters/21.txt)  
353. [ADguard Widgets filter (windows)](https://filters.adtidy.org/windows/filters/22.txt)  
354. [Easylist (windows)](https://filters.adtidy.org/windows/filters/101.txt)  
355. [Easylist China (windows)](https://filters.adtidy.org/windows/filters/104.txt)  
356. [EasyPrivacy (windows)](https://filters.adtidy.org/windows/filters/118.txt)  
357. [Fanboy's Annoyances (windows)](https://filters.adtidy.org/windows/filters/122.txt)  
358. [Fanboy's Social Blocking List (windows)](https://filters.adtidy.org/windows/filters/123.txt)  
359. [Web Annoyances Ultralist (windows)](https://filters.adtidy.org/windows/filters/201.txt)  
360. [Peter Lowe's Blocklist (windows)](https://filters.adtidy.org/windows/filters/204.txt)  
361. [Adblock Warning Removal List (windows)](https://filters.adtidy.org/windows/filters/207.txt)  
362. [Online Malicious URL Blocklist (windows)](https://filters.adtidy.org/windows/filters/208.txt)  
363. [ADgk Mobile China list (windows)](https://filters.adtidy.org/windows/filters/209.txt)  
364. [CJX's Annoyances List (windows)](https://filters.adtidy.org/windows/filters/220.txt)  
365. [ADguard Chinese filter (windows)](https://filters.adtidy.org/windows/filters/224.txt)  
366. [xinggsf (windows)](https://filters.adtidy.org/windows/filters/228.txt)  
367. [Fanboy's Anti-thirdparty Fonts (windows)](https://filters.adtidy.org/windows/filters/239.txt)  
368. [BarbBlock (windows)](https://filters.adtidy.org/windows/filters/240.txt)  
369. [EasyList Cookie List (windows)](https://filters.adtidy.org/windows/filters/241.txt)  
370. [NoCoin Filter List (windows)](https://filters.adtidy.org/windows/filters/242.txt)  
371. [Dandelion Sprout's Annoyances List (windows)](https://filters.adtidy.org/windows/filters/250.txt)  
372. [Legitimate URL Shortener (windows)](https://filters.adtidy.org/windows/filters/251.txt)  
373. [Phishing URL Blocklist (windows)](https://filters.adtidy.org/windows/filters/255.txt)  
374. [Scam Blocklist (windows)](https://filters.adtidy.org/windows/filters/256.txt)  
375. [uBlock Origin - Badware risks (windows)](https://filters.adtidy.org/windows/filters/257.txt)  
376. [ADguard Base filter (android)](https://filters.adtidy.org/android/filters/2_optimized.txt)  
377. [ADguard Tracking Protection filter (android)](https://filters.adtidy.org/android/filters/3_optimized.txt)  
378. [ADguard Social Media filter (android)](https://filters.adtidy.org/android/filters/4_optimized.txt)  
379. [ADguard Mobile Ads filter (android)](https://filters.adtidy.org/android/filters/11_optimized.txt)  
380. [ADguard Annoyances filter (android)](https://filters.adtidy.org/android/filters/14_optimized.txt)  
381. [ADguard DNS filter (android)](https://filters.adtidy.org/android/filters/15_optimized.txt)  
382. [ADguard URL Tracking filter (android)](https://filters.adtidy.org/android/filters/17_optimized.txt)  
383. [ADguard Cookie Notices filter (android)](https://filters.adtidy.org/android/filters/18_optimized.txt)  
384. [ADguard Popups filter (android)](https://filters.adtidy.org/android/filters/19_optimized.txt)  
385. [ADguard Mobile App Banners filter (android)](https://filters.adtidy.org/android/filters/20_optimized.txt)  
386. [ADguard Other Annoyances filter (android)](https://filters.adtidy.org/android/filters/21_optimized.txt)  
387. [ADguard Widgets filter (android)](https://filters.adtidy.org/android/filters/22_optimized.txt)  
388. [Easylist (android)](https://filters.adtidy.org/android/filters/101_optimized.txt)  
389. [Easylist China (android)](https://filters.adtidy.org/android/filters/104_optimized.txt)  
390. [EasyPrivacy (android)](https://filters.adtidy.org/android/filters/118_optimized.txt)  
391. [Fanboy's Annoyances (android)](https://filters.adtidy.org/android/filters/122_optimized.txt)
392. [Fanboy's Social Blocking List (android)](https://filters.adtidy.org/android/filters/123_optimized.txt)
393. [Web Annoyances Ultralist (android)](https://filters.adtidy.org/android/filters/201_optimized.txt)
394. [Peter Lowe's Blocklist (android)](https://filters.adtidy.org/android/filters/204_optimized.txt)
395. [Adblock Warning Removal List (android)](https://filters.adtidy.org/android/filters/207_optimized.txt)
396. [Online Malicious URL Blocklist (android)](https://filters.adtidy.org/android/filters/208_optimized.txt)
397. [ADgk Mobile China list (android)](https://filters.adtidy.org/android/filters/209_optimized.txt)
398. [CJX's Annoyances List (android)](https://filters.adtidy.org/android/filters/220_optimized.txt)
399. [ADguard Chinese filter (android)](https://filters.adtidy.org/android/filters/224_optimized.txt)
400. [xinggsf (android)](https://filters.adtidy.org/android/filters/228_optimized.txt)
401. [Fanboy's Anti-thirdparty Fonts (android)](https://filters.adtidy.org/android/filters/239_optimized.txt)
402. [BarbBlock (android)](https://filters.adtidy.org/android/filters/240_optimized.txt)
403. [EasyList Cookie List (android)](https://filters.adtidy.org/android/filters/241_optimized.txt)
404. [NoCoin Filter List (android)](https://filters.adtidy.org/android/filters/242_optimized.txt)
405. [Dandelion Sprout's Annoyances List (android)](https://filters.adtidy.org/android/filters/250_optimized.txt)
406. [Legitimate URL Shortener (android)](https://filters.adtidy.org/android/filters/251_optimized.txt)
407. [Phishing URL Blocklist (android)](https://filters.adtidy.org/android/filters/255_optimized.txt)
408. [Scam Blocklist (android)](https://filters.adtidy.org/android/filters/256_optimized.txt)
409. [uBlock Origin - Badware risks (android)](https://filters.adtidy.org/android/filters/257_optimized.txt)
410. [ADguard Base filter (ios)](https://filters.adtidy.org/ios/filters/2_optimized.txt)
411. [ADguard Tracking Protection filter (ios)](https://filters.adtidy.org/ios/filters/3_optimized.txt)
412. [ADguard Social Media filter (ios)](https://filters.adtidy.org/ios/filters/4_optimized.txt)
413. [ADguard Mobile Ads filter (ios)](https://filters.adtidy.org/ios/filters/11_optimized.txt)
414. [ADguard Annoyances filter (ios)](https://filters.adtidy.org/ios/filters/14_optimized.txt)
415. [ADguard DNS filter (ios)](https://filters.adtidy.org/ios/filters/15_optimized.txt)
416. [ADguard URL Tracking filter (ios)](https://filters.adtidy.org/ios/filters/17_optimized.txt)
417. [ADguard Cookie Notices filter (ios)](https://filters.adtidy.org/ios/filters/18_optimized.txt)
418. [ADguard Popups filter (ios)](https://filters.adtidy.org/ios/filters/19_optimized.txt)
419. [ADguard Mobile App Banners filter (ios)](https://filters.adtidy.org/ios/filters/20_optimized.txt)
420. [ADguard Other Annoyances filter (ios)](https://filters.adtidy.org/ios/filters/21_optimized.txt)
421. [ADguard Widgets filter (ios)](https://filters.adtidy.org/ios/filters/22_optimized.txt)
422. [Easylist (ios)](https://filters.adtidy.org/ios/filters/101_optimized.txt)
423. [Easylist China (ios)](https://filters.adtidy.org/ios/filters/104_optimized.txt)
424. [EasyPrivacy (ios)](https://filters.adtidy.org/ios/filters/118_optimized.txt)
425. [Fanboy's Annoyances (ios)](https://filters.adtidy.org/ios/filters/122_optimized.txt)
426. [Fanboy's Social Blocking List (ios)](https://filters.adtidy.org/ios/filters/123_optimized.txt)
427. [Web Annoyances Ultralist (ios)](https://filters.adtidy.org/ios/filters/201_optimized.txt)
428. [Peter Lowe's Blocklist (ios)](https://filters.adtidy.org/ios/filters/204_optimized.txt)
429. [Adblock Warning Removal List (ios)](https://filters.adtidy.org/ios/filters/207_optimized.txt)
430. [Online Malicious URL Blocklist (ios)](https://filters.adtidy.org/ios/filters/208_optimized.txt)
431. [ADgk Mobile China list (ios)](https://filters.adtidy.org/ios/filters/209_optimized.txt)
432. [CJX's Annoyances List (ios)](https://filters.adtidy.org/ios/filters/220_optimized.txt)
433. [ADguard Chinese filter (ios)](https://filters.adtidy.org/ios/filters/224_optimized.txt)
434. [xinggsf (ios)](https://filters.adtidy.org/ios/filters/228_optimized.txt)
435. [Fanboy's Anti-thirdparty Fonts (ios)](https://filters.adtidy.org/ios/filters/239_optimized.txt)
436. [BarbBlock (ios)](https://filters.adtidy.org/ios/filters/240_optimized.txt)
437. [EasyList Cookie List (ios)](https://filters.adtidy.org/ios/filters/241_optimized.txt)
438. [NoCoin Filter List (ios)](https://filters.adtidy.org/ios/filters/242_optimized.txt)
439. [Dandelion Sprout's Annoyances List (ios)](https://filters.adtidy.org/ios/filters/250_optimized.txt)
440. [Legitimate URL Shortener (ios)](https://filters.adtidy.org/ios/filters/251_optimized.txt)
441. [Phishing URL Blocklist (ios)](https://filters.adtidy.org/ios/filters/255_optimized.txt)
442. [Scam Blocklist (ios)](https://filters.adtidy.org/ios/filters/256_optimized.txt)
443. [uBlock Origin - Badware risks (ios)](https://filters.adtidy.org/ios/filters/257_optimized.txt)
444. [RPiList phishing-Angriffe](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Phishing-Angriffe)
445. [RPiList malware](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/malware)
446. [RPiList spam mails](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/spam.mails)
447. [adaway](https://adaway.org/hosts.txt)


</details>

## 五、特别致谢


<details>
  <summary>致谢名单</summary>

1. [anti-AD](https://github.com/privacy-protection-tools/anti-AD)
2. [easylist](https://github.com/easylist/easylist)
3. [oisd](https://github.com/sjhgvr/oisd)
4. [cjxlist](https://github.com/cjx82630/cjxlist)
5. [uniartisan](https://github.com/uniartisan/adblock_list)
6. [Cats-Team](https://github.com/Cats-Team/AdRules)
7. [217heidai](https://github.com/217heidai/adblockfilters)
8. [GOODBYEADS](https://github.com/8680/GOODBYEADS)
9. [AWAvenue-Ads-Rule](https://github.com/TG-Twilight/AWAvenue-Ads-Rule)
10. [uBlockOrigin](https://github.com/uBlockOrigin/uAssets)
11. [ADguardTeam](https://github.com/AdguardTeam/AdGuardFilters)
12. [HyperADRules](https://github.com/Lynricsy/HyperADRules)
13. [xinggsf](https://github.com/xinggsf/Adblock-Plus-Rule)
14. [hoshsadiq](https://github.com/hoshsadiq/adblock-nocoin-list)
15. [malware-filter](https://gitlab.com/malware-filter)
16. [abp-filters](https://gitlab.com/eyeo/anti-cv/abp-filters-anti-cv)
17. [banbendalao](https://github.com/banbendalao/ADgk)
18. [yokoffing](https://github.com/yokoffing/filterlists)
19. [Spam404](https://github.com/Spam404/lists)
20. [brave](https://github.com/brave/adblock-lists)
21. [Peter Lowe](https://pgl.yoyo.org/adservers/)
22. [DandelionSprout](https://github.com/DandelionSprout/adfilt)
23. [blocklistproject](https://github.com/blocklistproject/Lists)
24. [reek](https://github.com/reek/anti-adblock-killer)
25. [durablenapkin](https://github.com/durablenapkin/scamblocklist)
26. [Perflyst](https://github.com/Perflyst/PiHoleBlocklist)
27. [hagezi](https://github.com/hagezi/dns-blocklists)
28. [neodevpro](https://github.com/neodevpro/neodevhost)
29. [damengzhu](https://github.com/damengzhu/banad)
30. [hectorm](https://github.com/hectorm/hblock)
31. [badmojr](https://github.com/badmojr/1Hosts)
32. [paulgb](https://github.com/paulgb/BarbBlock)
33. [Adblocker](https://adblockultimate.net/filters)
34. [RPiList](https://github.com/RPiList/specials)
35. [adaway](https://github.com/AdAway/AdAway)

 </details>






<br>
<br>


## LICENSE
- [CC-BY-NC-SA 4.0 License](https://github.com/REIJI007/Adblock-Rule-Collection/blob/main/LICENSE-CC-BY-NC-SA%204.0)
- [GPL-3.0 License](https://github.com/REIJI007/Adblock-Rule-Collection/blob/main/LICENSE-GPL3.0)
