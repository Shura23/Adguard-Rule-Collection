[![GPL 3.0 license](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://github.com/REIJI007/Adblock-Rule-Collection/blob/main/LICENSE-GPL%203.0)
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

*Host IPV6列表*
<table border="1" style="border-collapse: collapse; width: 100%;">
  <tr>
    <th>版本</th>
    <th>链接</th>
  </tr>
  <tr>
    <td>完整版</td>
    <td>
      <strong><a href="https://raw.githubusercontent.com/REIJI007/Adblock-Rule-Collection/main/ADBLOCK_RULE_COLLECTION_HOST_IPV6.txt">Github原始链接</a></strong> | 
      <strong><a href="https://adblock-host-ipv6.reiji007.org/">Cloudflare加速链接</a></strong>
    </td>
  </tr>
  <tr>
    <td>精简版</td>
    <td>
      <strong><a href="https://raw.githubusercontent.com/REIJI007/Adblock-Rule-Collection/main/ADBLOCK_RULE_COLLECTION_HOST_IPV6_Lite.txt">Github原始链接</a></strong> | 
      <strong><a href="https://adblock-host-ipv6-lite.reiji007.org/">Cloudflare加速链接</a></strong>
    </td>
  </tr>
</table>

2、从Release中下载过滤器文件进行本地导入过滤器，release每20分钟自动发布一次
<hr>


## 三、适用范围
适用于ADguard,Adblock Plus,uBlock Origin,Brave Browser等各类符合Adblock Plus 语法、uBlock Origin 语法、AdGuard 语法的浏览器插件或广告拦截程序以及DNS服务器
<br>


## 四、汇总引用规则列表有如下
<details>
  <summary>规则列表</summary>

1. [Adaway](https://adaway.org/hosts.txt)
2. [urlhaus](https://urlhaus.abuse.ch/downloads/hostfile)
3. [ADguard Base filter](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_2_Base/filter.txt)
4. [ADguard Spyware filter](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_3_Spyware/filter.txt)
5. [ADguard Social filter](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_4_Social/filter.txt)
6. [ADguard Mobile filter](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_11_Mobile/filter.txt)
7. [ADguard Annoyances filter](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_14_Annoyances/filter.txt)
8. [ADguard Dns Filter](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_15_DnsFilter/filter.txt)
9. [ADguard TrackParam filter](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_17_TrackParam/filter.txt)
10. [ADguard Annoyances_Cookies filter](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_18_Annoyances_Cookies/filter.txt)
11. [ADguard Annoyances_Popups filter](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_19_Annoyances_Popups/filter.txt)
12. [ADguard Annoyances_MobileApp filter](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_20_Annoyances_MobileApp/filter.txt)
13. [ADguard Annoyances_Other filter](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_21_Annoyances_Other/filter.txt)
14. [ADguard Annoyances_Widgets filter](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_22_Annoyances_Widgets/filter.txt)
15. [ADguard Chinese filter](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_224_Chinese/filter.txt)
16. [ADguard ThirdParty EasyList](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_101_EasyList/filter.txt)
17. [ADguard ThirdParty EasyListChina](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_104_EasyListChina/filter.txt)
18. [ADguard ThirdParty EasyPrivacy](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_118_EasyPrivacy/filter.txt)
19. [ADguard ThirdParty Fanboy's Annoyance List](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_122_FanboysAnnoyances/filter.txt)
20. [ADguard ThirdParty FanboysSocialBlockingList](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_123_FanboysSocialBlockingList/filter.txt)
21. [ADguard ThirdParty WebAnnoyancesUltralist](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_201_WebAnnoyancesUltralist/filter.txt)
22. [ADguard ThirdParty PeterLowesList](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_204_PeterLowesList/filter.txt)
23. [ADguard ThirdParty AdblockWarningRemovalList](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_207_AdblockWarningRemovalList/filter.txt)
24. [ADguard ThirdParty Online_Malicious_URL_Blocklist](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_208_Online_Malicious_URL_Blocklist/filter.txt)
25. [ADguard ThirdParty ADgkMobileChinalist](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_209_ADgkMobileChinalist/filter.txt)
26. [ADguard ThirdParty Spam404](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_210_Spam404/filter.txt)
27. [ADguard ThirdParty Anti-Adblock Killer](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_211_AntiAdblockKillerReek/filter.txt)
28. [ADguard ThirdParty ChinaListAndEasyList](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_219_ChinaListAndEasyList/filter.txt)
29. [ADguard ThirdParty CJXsAnnoyanceList](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_220_CJXsAnnoyanceList/filter.txt)
30. [ADguard ThirdParty xinggsf](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_228_xinggsf/filter.txt)
31. [ADguard ThirdParty IdontCareAboutCookies](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_229_IdontCareAboutCookies/filter.txt)
32. [ADguard ThirdParty FanboyAntifonts](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_239_FanboyAntifonts/filter.txt)
33. [ADguard ThirdParty BarbBlock](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_240_BarbBlock/filter.txt)
34. [ADguard ThirdParty FanboyCookiemonster](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_241_FanboyCookiemonster/filter.txt)
35. [ADguard ThirdParty NoCoin](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_242_NoCoin/filter.txt)
36. [ADguard ThirdParty DandelionSproutAnnoyances](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_250_DandelionSproutAnnoyances/filter.txt)
37. [ADguard ThirdParty Legitimate_URL_Shortener](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_251_LegitimateURLShortener/filter.txt)
38. [ADguard ThirdParty Phishing_URL_Blocklist](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_255_Phishing_URL_Blocklist/filter.txt)
39. [ADguard ThirdParty Scam_Blocklist](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_256_Scam_Blocklist/filter.txt)
40. [ADguard ThirdParty uBlock_Origin_Badware_risks](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/ThirdParty/filter_257_uBlock_Origin_Badware_risks/filter.txt)
41. [ADguard Base filterâ€”first-party servers](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/BaseFilter/sections/adservers_firstparty.txt)
42. [ADguard Base filterâ€”foreign servers](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/BaseFilter/sections/foreign.txt)
43. [ADguard Base filter-cryptominers](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/BaseFilter/sections/cryptominers.txt)
44. [ADguard Base filter-adservers](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/BaseFilter/sections/adservers.txt)
45. [ADguard Base filter-adservers_firstparty](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/BaseFilter/sections/adservers_firstparty.txt)
46. [ADguard Base filter-allowlist](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/BaseFilter/sections/allowlist.txt)
47. [ADguard Base filter-allowlist_stealth](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/BaseFilter/sections/allowlist_stealth.txt)
48. [ADguard Base filter-antiadblock](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/BaseFilter/sections/antiadblock.txt)
49. [ADguard Base filter-replace](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/BaseFilter/sections/replace.txt)
50. [ADguard Base filter-content_blocker](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/BaseFilter/sections/content_blocker.txt)
51. [ADguard Exclusion rules](https://raw.githubusercontent.com/AdguardTeam/ADguardSDNSFilter/master/Filters/exclusions.txt)  
52. [ADguard Exception rules](https://raw.githubusercontent.com/AdguardTeam/ADguardSDNSFilter/master/Filters/exceptions.txt)  
53. [ADguard SDNSFilter rules](https://raw.githubusercontent.com/AdguardTeam/ADguardSDNSFilter/master/Filters/rules.txt)  
54. [ADguard Tracking Protection filter — first-party trackers](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SpywareFilter/sections/tracking_servers_firstparty.txt)  
55. [ADguard Tracking Protection filter — third-party trackers](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SpywareFilter/sections/tracking_servers.txt)  
56. [ADguard Tracking Protection filter — mobile trackers](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SpywareFilter/sections/mobile.txt)  
57. [ADguard Social filter-allowlist](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SocialFilter/sections/allowlist.txt)  
58. [ADguard Social filter-general_elemhide](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SocialFilter/sections/general_elemhide.txt)  
59. [ADguard Social filter-general_extensions](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SocialFilter/sections/general_extensions.txt)  
60. [ADguard Social filter-general_url](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SocialFilter/sections/general_url.txt)  
61. [ADguard Social filter-popups](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SocialFilter/sections/popups.txt)  
62. [ADguard Social filter-social_trackers](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SocialFilter/sections/social_trackers.txt)  
63. [ADguard Annoyances filter-cookies_allowlist](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/Cookies/sections/cookies_allowlist.txt)  
64. [ADguard Annoyances filter-cookies_general](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/Cookies/sections/cookies_general.txt)  
65. [ADguard Annoyances filter-mobile-app_allowlist](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/MobileApp/sections/mobile-app_allowlist.txt)  
66. [ADguard Annoyances filter-mobile-app_general](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/MobileApp/sections/mobile-app_general.txt)  
67. [ADguard Annoyances filter-popups-antiadblock](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/Popups/sections/antiadblock.txt)  
68. [ADguard Annoyances filter-popups-allowlist](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/Popups/sections/popups_allowlist.txt)  
69. [ADguard Annoyances filter-popups-general](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/Popups/sections/popups_general.txt)  
70. [ADguard Annoyances filter-popups-push-notifications_allowlist](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/Popups/sections/push-notifications_allowlist.txt)  
71. [ADguard Annoyances filter-popups-push-notifications_general](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/Popups/sections/push-notifications_general.txt)  
72. [ADguard Annoyances filter-popups-subscriptions_allowlist](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/Popups/sections/subscriptions_allowlist.txt)  
73. [ADguard Annoyances filter-popups-subscriptions_general](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/Popups/sections/subscriptions_general.txt)  
74. [ADguard Annoyances filter-Widgets](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/AnnoyancesFilter/Widgets/sections/widgets.txt)  
75. [ADguard CNAME original trackers list](https://raw.githubusercontent.com/AdguardTeam/cname-trackers/master/data/combined_original_trackers.txt)  
76. [ADguard CNAME disguised ads list](https://raw.githubusercontent.com/AdguardTeam/cname-trackers/master/data/combined_disguised_ads.txt)  
77. [ADguard CNAME disguised clickthroughs list](https://raw.githubusercontent.com/AdguardTeam/cname-trackers/master/data/combined_disguised_clickthroughs.txt)  
78. [ADguard CNAME disguised microsites list](https://raw.githubusercontent.com/AdguardTeam/cname-trackers/master/data/combined_disguised_microsites.txt)  
79. [ADguard CNAME disguised trackers list](https://raw.githubusercontent.com/AdguardTeam/cname-trackers/master/data/combined_disguised_trackers.txt)  
80. [ADguard CNAME disguised mail_trackers list](https://raw.githubusercontent.com/AdguardTeam/cname-trackers/master/data/combined_disguised_mail_trackers.txt)  
81. [ADguard Chinese filter-adservers](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/ChineseFilter/sections/adservers.txt)  
82. [ADguard Chinese filter-adservers_firstparty](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/ChineseFilter/sections/adservers_firstparty.txt)  
83. [ADguard ChineseFilter-allowlist](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/ChineseFilter/sections/allowlist.txt)  
84. [ADguard ChineseFilter-antiadblock](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/ChineseFilter/sections/antiadblock.txt)  
85. [ADguard ChineseFilter-general_elemhide](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/ChineseFilter/sections/general_elemhide.txt)  
86. [ADguard ChineseFilter-general_extensions](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/ChineseFilter/sections/general_extensions.txt)  
87. [ADguard ChineseFilter-general_url](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/ChineseFilter/sections/general_url.txt)  
88. [ADguard ChineseFilter-replace](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/ChineseFilter/sections/replace.txt)  
89. [ADguard Mobile filter-adservers](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/MobileFilter/sections/adservers.txt)  
90. [ADguard MobileFilter-allowlist_app](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/MobileFilter/sections/allowlist_app.txt)  
91. [ADguard MobileFilter-allowlist_web](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/MobileFilter/sections/allowlist_web.txt)  
92. [ADguard MobileFilter-antiadblock](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/MobileFilter/sections/antiadblock.txt)  
93. [ADguard MobileFilter-general_elemhide](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/MobileFilter/sections/general_elemhide.txt)  
94. [ADguard MobileFilter-general_extensions](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/MobileFilter/sections/general_extensions.txt)  
95. [ADguard MobileFilter-general_url](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/MobileFilter/sections/general_url.txt)  
96. [ADguard MobileFilter-replace](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/MobileFilter/sections/replace.txt)  
97. [ADguard SpywareFilter-allowlist](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SpywareFilter/sections/allowlist.txt)  
98. [ADguard SpywareFilter-cookies_allowlist](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SpywareFilter/sections/cookies_allowlist.txt)  
99. [ADguard SpywareFilter-cookies_general](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SpywareFilter/sections/cookies_general.txt)  
100. [ADguard SpywareFilter-cookies_specific](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SpywareFilter/sections/cookies_specific.txt)  
101. [ADguard SpywareFilter-general_elemhide](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SpywareFilter/sections/general_elemhide.txt)  
102. [ADguard SpywareFilter-general_extensions](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SpywareFilter/sections/general_extensions.txt)  
103. [ADguard SpywareFilter-general_url](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SpywareFilter/sections/general_url.txt)  
104. [ADguard SpywareFilter-mobile](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SpywareFilter/sections/mobile.txt)  
105. [ADguard SpywareFilter-mobile_allowlist](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SpywareFilter/sections/mobile_allowlist.txt)  
106. [ADguard SpywareFilter-tracking_servers](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SpywareFilter/sections/tracking_servers.txt)  
107. [ADguard SpywareFilter-tracking_servers_firstparty](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/SpywareFilter/sections/tracking_servers_firstparty.txt)  
108. [ADguard TrackParamFilter-allowlist](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/TrackParamFilter/sections/allowlist.txt)  
109. [ADguard TrackParamFilter-general_url](https://raw.githubusercontent.com/AdguardTeam/ADguardFilters/master/TrackParamFilter/sections/general_url.txt)  
110. [uBlock filters](https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt)  
111. [uBlock privacy filter](https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt)  
112. [uBlock mobile filter](https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-mobile.txt)  
113. [uBlock Badware risks filter](https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt)  
114. [uBlock Annoyances-Cookies filter](https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances-cookies.txt)  
115. [uBlock Annoyances-others filter](https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances-others.txt)  
116. [uBlock Resource abuse filters](https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt)  
117. [uBlock Unbreak filter](https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt)  
118. [uBlock lan-block](https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/lan-block.txt)  
119. [ADblocker Ultimate Ad Filter](https://filters.adavoid.org/ultimate-ad-filter.txt)  
120. [ADblocker Ultimate Privacy Filter](https://filters.adavoid.org/ultimate-privacy-filter.txt)  
121. [ADblocker Ultimate Security Filter](https://filters.adavoid.org/ultimate-security-filter.txt)  
122. [ADguard Base filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/2.txt)  
123. [ADguard Tracking Protection filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/3.txt)  
124. [ADguard Social Media filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/4.txt)  
125. [ADguard Mobile Ads filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/11.txt)  
126. [ADguard Annoyances filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/14.txt)  
127. [ADguard DNS filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/15.txt)  
128. [ADguard URL Tracking filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/17.txt)  
129. [ADguard Cookie Notices filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/18.txt)  
130. [ADguard Popups filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/19.txt)  
131. [ADguard Mobile App Banners filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/20.txt)  
132. [ADguard Other Annoyances filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/21.txt)  
133. [ADguard Widgets filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/22.txt)  
134. [Easylist (ublock)](https://filters.adtidy.org/extension/ublock/filters/101.txt)  
135. [Easylist China (ublock)](https://filters.adtidy.org/extension/ublock/filters/104.txt)  
136. [EasyPrivacy (ublock)](https://filters.adtidy.org/extension/ublock/filters/118.txt)  
137. [Fanboy's Annoyances (ublock)](https://filters.adtidy.org/extension/ublock/filters/122.txt)  
138. [Fanboy's Social Blocking List (ublock)](https://filters.adtidy.org/extension/ublock/filters/123.txt)  
139. [Web Annoyances Ultralist (ublock)](https://filters.adtidy.org/extension/ublock/filters/201.txt)  
140. [Peter Lowe's Blocklist (ublock)](https://filters.adtidy.org/extension/ublock/filters/204.txt)  
141. [Adblock Warning Removal List (ublock)](https://filters.adtidy.org/extension/ublock/filters/207.txt)  
142. [Online Malicious URL Blocklist (ublock)](https://filters.adtidy.org/extension/ublock/filters/208.txt)  
143. [ADgk Mobile China list (ublock)](https://filters.adtidy.org/extension/ublock/filters/209.txt)  
144. [CJX's Annoyances List (ublock)](https://filters.adtidy.org/extension/ublock/filters/220.txt)  
145. [ADguard Chinese filter (ublock)](https://filters.adtidy.org/extension/ublock/filters/224.txt)  
146. [xinggsf (ublock)](https://filters.adtidy.org/extension/ublock/filters/228.txt)  
147. [Fanboy's Anti-thirdparty Fonts (ublock)](https://filters.adtidy.org/extension/ublock/filters/239.txt)  
148. [BarbBlock (ublock)](https://filters.adtidy.org/extension/ublock/filters/240.txt)  
149. [EasyList Cookie List (ublock)](https://filters.adtidy.org/extension/ublock/filters/241.txt)  
150. [NoCoin Filter List (ublock)](https://filters.adtidy.org/extension/ublock/filters/242.txt)
151. [Dandelion Sprout's Annoyances List (ublock)](https://filters.adtidy.org/extension/ublock/filters/250.txt)  
152. [Legitimate URL Shortener (ublock)](https://filters.adtidy.org/extension/ublock/filters/251.txt)  
153. [Phishing URL Blocklist (ublock)](https://filters.adtidy.org/extension/ublock/filters/255.txt)  
154. [Scam Blocklist (ublock)](https://filters.adtidy.org/extension/ublock/filters/256.txt)  
155. [uBlock Origin – Badware risks (ublock)](https://filters.adtidy.org/extension/ublock/filters/257.txt)  
156. [ADguard Base filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/2.txt)  
157. [ADguard Tracking Protection filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/3.txt)  
158. [ADguard Social Media filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/4.txt)  
159. [ADguard Mobile Ads filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/11.txt)  
160. [ADguard Annoyances filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/14.txt)  
161. [ADguard DNS filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/15.txt)  
162. [ADguard URL Tracking filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/17.txt)  
163. [ADguard Cookie Notices filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/18.txt)  
164. [ADguard Popups filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/19.txt)  
165. [ADguard Mobile App Banners filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/20.txt)  
166. [ADguard Other Annoyances filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/21.txt)  
167. [ADguard Widgets filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/22.txt)  
168. [Easylist (chromium)](https://filters.adtidy.org/extension/chromium/filters/101.txt)  
169. [Easylist China (chromium)](https://filters.adtidy.org/extension/chromium/filters/104.txt)  
170. [EasyPrivacy (chromium)](https://filters.adtidy.org/extension/chromium/filters/118.txt)  
171. [Fanboy's Annoyances (chromium)](https://filters.adtidy.org/extension/chromium/filters/122.txt)  
172. [Fanboy's Social Blocking List (chromium)](https://filters.adtidy.org/extension/chromium/filters/123.txt)  
173. [Web Annoyances Ultralist (chromium)](https://filters.adtidy.org/extension/chromium/filters/201.txt)  
174. [Peter Lowe's Blocklist (chromium)](https://filters.adtidy.org/extension/chromium/filters/204.txt)  
175. [Adblock Warning Removal List (chromium)](https://filters.adtidy.org/extension/chromium/filters/207.txt)  
176. [Online Malicious URL Blocklist (chromium)](https://filters.adtidy.org/extension/chromium/filters/208.txt)  
177. [ADgk Mobile China list (chromium)](https://filters.adtidy.org/extension/chromium/filters/209.txt)  
178. [CJX's Annoyances List (chromium)](https://filters.adtidy.org/extension/chromium/filters/220.txt)  
179. [ADguard Chinese filter (chromium)](https://filters.adtidy.org/extension/chromium/filters/224.txt)  
180. [xinggsf (chromium)](https://filters.adtidy.org/extension/chromium/filters/228.txt)  
181. [Fanboy's Anti-thirdparty Fonts (chromium)](https://filters.adtidy.org/extension/chromium/filters/239.txt)  
182. [BarbBlock (chromium)](https://filters.adtidy.org/extension/chromium/filters/240.txt)  
183. [EasyList Cookie List (chromium)](https://filters.adtidy.org/extension/chromium/filters/241.txt)  
184. [NoCoin Filter List (chromium)](https://filters.adtidy.org/extension/chromium/filters/242.txt)  
185. [Dandelion Sprout's Annoyances List (chromium)](https://filters.adtidy.org/extension/chromium/filters/250.txt)  
186. [Legitimate URL Shortener (chromium)](https://filters.adtidy.org/extension/chromium/filters/251.txt)  
187. [Phishing URL Blocklist (chromium)](https://filters.adtidy.org/extension/chromium/filters/255.txt)  
188. [Scam Blocklist (chromium)](https://filters.adtidy.org/extension/chromium/filters/256.txt)  
189. [uBlock Origin – Badware risks (chromium)](https://filters.adtidy.org/extension/chromium/filters/257.txt)  
190. [ADguard Base filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/2.txt)  
191. [ADguard Tracking Protection filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/3.txt)  
192. [ADguard Social Media filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/4.txt)  
193. [ADguard Mobile Ads filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/11.txt)  
194. [ADguard Annoyances filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/14.txt)  
195. [ADguard DNS filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/15.txt)  
196. [ADguard URL Tracking filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/17.txt)  
197. [ADguard Cookie Notices filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/18.txt)  
198. [ADguard Popups filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/19.txt)  
199. [ADguard Mobile App Banners filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/20.txt)  
200. [ADguard Other Annoyances filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/21.txt)
201. [ADguard Widgets filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/22.txt)  
202. [Easylist (firefox)](https://filters.adtidy.org/extension/firefox/filters/101.txt)  
203. [Easylist China (firefox)](https://filters.adtidy.org/extension/firefox/filters/104.txt)  
204. [EasyPrivacy (firefox)](https://filters.adtidy.org/extension/firefox/filters/118.txt)  
205. [Fanboy's Annoyances (firefox)](https://filters.adtidy.org/extension/firefox/filters/122.txt)  
206. [Fanboy's Social Blocking List (firefox)](https://filters.adtidy.org/extension/firefox/filters/123.txt)  
207. [Web Annoyances Ultralist (firefox)](https://filters.adtidy.org/extension/firefox/filters/201.txt)  
208. [Peter Lowe's Blocklist (firefox)](https://filters.adtidy.org/extension/firefox/filters/204.txt)  
209. [Adblock Warning Removal List (firefox)](https://filters.adtidy.org/extension/firefox/filters/207.txt)  
210. [Online Malicious URL Blocklist (firefox)](https://filters.adtidy.org/extension/firefox/filters/208.txt)  
211. [ADgk Mobile China list (firefox)](https://filters.adtidy.org/extension/firefox/filters/209.txt)  
212. [CJX's Annoyances List (firefox)](https://filters.adtidy.org/extension/firefox/filters/220.txt)  
213. [ADguard Chinese filter (firefox)](https://filters.adtidy.org/extension/firefox/filters/224.txt)  
214. [xinggsf (firefox)](https://filters.adtidy.org/extension/firefox/filters/228.txt)  
215. [Fanboy's Anti-thirdparty Fonts (firefox)](https://filters.adtidy.org/extension/firefox/filters/239.txt)  
216. [BarbBlock (firefox)](https://filters.adtidy.org/extension/firefox/filters/240.txt)  
217. [EasyList Cookie List (firefox)](https://filters.adtidy.org/extension/firefox/filters/241.txt)  
218. [NoCoin Filter List (firefox)](https://filters.adtidy.org/extension/firefox/filters/242.txt)  
219. [Dandelion Sprout's Annoyances List (firefox)](https://filters.adtidy.org/extension/firefox/filters/250.txt)  
220. [Legitimate URL Shortener (firefox)](https://filters.adtidy.org/extension/firefox/filters/251.txt)  
221. [Phishing URL Blocklist (firefox)](https://filters.adtidy.org/extension/firefox/filters/255.txt)  
222. [Scam Blocklist (firefox)](https://filters.adtidy.org/extension/firefox/filters/256.txt)  
223. [uBlock Origin – Badware risks (firefox)](https://filters.adtidy.org/extension/firefox/filters/257.txt)  
224. [ADguard Base filter (windows)](https://filters.adtidy.org/windows/filters/2.txt)  
225. [ADguard Tracking Protection filter (windows)](https://filters.adtidy.org/windows/filters/3.txt)  
226. [ADguard Social Media filter (windows)](https://filters.adtidy.org/windows/filters/4.txt)  
227. [ADguard Mobile Ads filter (windows)](https://filters.adtidy.org/windows/filters/11.txt)  
228. [ADguard Annoyances filter (windows)](https://filters.adtidy.org/windows/filters/14.txt)  
229. [ADguard DNS filter (windows)](https://filters.adtidy.org/windows/filters/15.txt)  
230. [ADguard URL Tracking filter (windows)](https://filters.adtidy.org/windows/filters/17.txt)  
231. [ADguard Cookie Notices filter (windows)](https://filters.adtidy.org/windows/filters/18.txt)  
232. [ADguard Popups filter (windows)](https://filters.adtidy.org/windows/filters/19.txt)  
233. [ADguard Mobile App Banners filter (windows)](https://filters.adtidy.org/windows/filters/20.txt)  
234. [ADguard Other Annoyances filter (windows)](https://filters.adtidy.org/windows/filters/21.txt)  
235. [ADguard Widgets filter (windows)](https://filters.adtidy.org/windows/filters/22.txt)  
236. [Easylist (windows)](https://filters.adtidy.org/windows/filters/101.txt)  
237. [Easylist China (windows)](https://filters.adtidy.org/windows/filters/104.txt)  
238. [EasyPrivacy (windows)](https://filters.adtidy.org/windows/filters/118.txt)  
239. [Fanboy's Annoyances (windows)](https://filters.adtidy.org/windows/filters/122.txt)  
240. [Fanboy's Social Blocking List (windows)](https://filters.adtidy.org/windows/filters/123.txt)  
241. [Web Annoyances Ultralist (windows)](https://filters.adtidy.org/windows/filters/201.txt)  
242. [Peter Lowe's Blocklist (windows)](https://filters.adtidy.org/windows/filters/204.txt)  
243. [Adblock Warning Removal List (windows)](https://filters.adtidy.org/windows/filters/207.txt)  
244. [Online Malicious URL Blocklist (windows)](https://filters.adtidy.org/windows/filters/208.txt)  
245. [ADgk Mobile China list (windows)](https://filters.adtidy.org/windows/filters/209.txt)  
246. [CJX's Annoyances List (windows)](https://filters.adtidy.org/windows/filters/220.txt)  
247. [ADguard Chinese filter (windows)](https://filters.adtidy.org/windows/filters/224.txt)  
248. [xinggsf (windows)](https://filters.adtidy.org/windows/filters/228.txt)  
249. [Fanboy's Anti-thirdparty Fonts (windows)](https://filters.adtidy.org/windows/filters/239.txt)  
250. [BarbBlock (windows)](https://filters.adtidy.org/windows/filters/240.txt)
251. [EasyList Cookie List (windows)](https://filters.adtidy.org/windows/filters/241.txt)  
252. [NoCoin Filter List (windows)](https://filters.adtidy.org/windows/filters/242.txt)  
253. [Dandelion Sprout's Annoyances List (windows)](https://filters.adtidy.org/windows/filters/250.txt)  
254. [Legitimate URL Shortener (windows)](https://filters.adtidy.org/windows/filters/251.txt)  
255. [Phishing URL Blocklist (windows)](https://filters.adtidy.org/windows/filters/255.txt)  
256. [Scam Blocklist (windows)](https://filters.adtidy.org/windows/filters/256.txt)  
257. [uBlock Origin – Badware risks (windows)](https://filters.adtidy.org/windows/filters/257.txt)  
258. [ADguard Base filter (android)](https://filters.adtidy.org/android/filters/2_optimized.txt)  
259. [ADguard Tracking Protection filter (android)](https://filters.adtidy.org/android/filters/3_optimized.txt)  
260. [ADguard Social Media filter (android)](https://filters.adtidy.org/android/filters/4_optimized.txt)  
261. [ADguard Mobile Ads filter (android)](https://filters.adtidy.org/android/filters/11_optimized.txt)  
262. [ADguard Annoyances filter (android)](https://filters.adtidy.org/android/filters/14_optimized.txt)  
263. [ADguard DNS filter (android)](https://filters.adtidy.org/android/filters/15_optimized.txt)  
264. [ADguard URL Tracking filter (android)](https://filters.adtidy.org/android/filters/17_optimized.txt)  
265. [ADguard Cookie Notices filter (android)](https://filters.adtidy.org/android/filters/18_optimized.txt)  
266. [ADguard Popups filter (android)](https://filters.adtidy.org/android/filters/19_optimized.txt)  
267. [ADguard Mobile App Banners filter (android)](https://filters.adtidy.org/android/filters/20_optimized.txt)  
268. [ADguard Other Annoyances filter (android)](https://filters.adtidy.org/android/filters/21_optimized.txt)  
269. [ADguard Widgets filter (android)](https://filters.adtidy.org/android/filters/22_optimized.txt)  
270. [Easylist (android)](https://filters.adtidy.org/android/filters/101_optimized.txt)  
271. [Easylist China (android)](https://filters.adtidy.org/android/filters/104_optimized.txt)  
272. [EasyPrivacy (android)](https://filters.adtidy.org/android/filters/118_optimized.txt)  
273. [Fanboy's Annoyances (android)](https://filters.adtidy.org/android/filters/122_optimized.txt)  
274. [Fanboy's Social Blocking List (android)](https://filters.adtidy.org/android/filters/123_optimized.txt)  
275. [Web Annoyances Ultralist (android)](https://filters.adtidy.org/android/filters/201_optimized.txt)  
276. [Peter Lowe's Blocklist (android)](https://filters.adtidy.org/android/filters/204_optimized.txt)  
277. [Adblock Warning Removal List (android)](https://filters.adtidy.org/android/filters/207_optimized.txt)  
278. [Online Malicious URL Blocklist (android)](https://filters.adtidy.org/android/filters/208_optimized.txt)  
279. [ADgk Mobile China list (android)](https://filters.adtidy.org/android/filters/209_optimized.txt)  
280. [CJX's Annoyances List (android)](https://filters.adtidy.org/android/filters/220_optimized.txt)  
281. [ADguard Chinese filter (android)](https://filters.adtidy.org/android/filters/224_optimized.txt)  
282. [xinggsf (android)](https://filters.adtidy.org/android/filters/228_optimized.txt)  
283. [Fanboy's Anti-thirdparty Fonts (android)](https://filters.adtidy.org/android/filters/239_optimized.txt)  
284. [BarbBlock (android)](https://filters.adtidy.org/android/filters/240_optimized.txt)  
285. [EasyList Cookie List (android)](https://filters.adtidy.org/android/filters/241_optimized.txt)  
286. [NoCoin Filter List (android)](https://filters.adtidy.org/android/filters/242_optimized.txt)  
287. [Dandelion Sprout's Annoyances List (android)](https://filters.adtidy.org/android/filters/250_optimized.txt)  
288. [Legitimate URL Shortener (android)](https://filters.adtidy.org/android/filters/251_optimized.txt)  
289. [Phishing URL Blocklist (android)](https://filters.adtidy.org/android/filters/255_optimized.txt)  
290. [Scam Blocklist (android)](https://filters.adtidy.org/android/filters/256_optimized.txt)  
291. [uBlock Origin – Badware risks (android)](https://filters.adtidy.org/android/filters/257_optimized.txt)  
292. [ADguard Base filter (ios)](https://filters.adtidy.org/ios/filters/2_optimized.txt)  
293. [ADguard Tracking Protection filter (ios)](https://filters.adtidy.org/ios/filters/3_optimized.txt)  
294. [ADguard Social Media filter (ios)](https://filters.adtidy.org/ios/filters/4_optimized.txt)  
295. [ADguard Mobile Ads filter (ios)](https://filters.adtidy.org/ios/filters/11_optimized.txt)  
296. [ADguard Annoyances filter (ios)](https://filters.adtidy.org/ios/filters/14_optimized.txt)  
297. [ADguard DNS filter (ios)](https://filters.adtidy.org/ios/filters/15_optimized.txt)  
298. [ADguard URL Tracking filter (ios)](https://filters.adtidy.org/ios/filters/17_optimized.txt)  
299. [ADguard Cookie Notices filter (ios)](https://filters.adtidy.org/ios/filters/18_optimized.txt)  
300. [ADguard Popups filter (ios)](https://filters.adtidy.org/ios/filters/19_optimized.txt)  
301. [ADguard Mobile App Banners filter (ios)](https://filters.adtidy.org/ios/filters/20_optimized.txt)  
302. [ADguard Other Annoyances filter (ios)](https://filters.adtidy.org/ios/filters/21_optimized.txt)  
303. [ADguard Widgets filter (ios)](https://filters.adtidy.org/ios/filters/22_optimized.txt)  
304. [Easylist (ios)](https://filters.adtidy.org/ios/filters/101_optimized.txt)  
305. [Easylist China (ios)](https://filters.adtidy.org/ios/filters/104_optimized.txt)  
306. [EasyPrivacy (ios)](https://filters.adtidy.org/ios/filters/118_optimized.txt)  
307. [Fanboy's Annoyances (ios)](https://filters.adtidy.org/ios/filters/122_optimized.txt)  
308. [Fanboy's Social Blocking List (ios)](https://filters.adtidy.org/ios/filters/123_optimized.txt)  
309. [Web Annoyances Ultralist (ios)](https://filters.adtidy.org/ios/filters/201_optimized.txt)  
310. [Peter Lowe's Blocklist (ios)](https://filters.adtidy.org/ios/filters/204_optimized.txt)  
311. [Adblock Warning Removal List (ios)](https://filters.adtidy.org/ios/filters/207_optimized.txt)  
312. [Online Malicious URL Blocklist (ios)](https://filters.adtidy.org/ios/filters/208_optimized.txt)  
313. [ADgk Mobile China list (ios)](https://filters.adtidy.org/ios/filters/209_optimized.txt)  
314. [CJX's Annoyances List (ios)](https://filters.adtidy.org/ios/filters/220_optimized.txt)  
315. [ADguard Chinese filter (ios)](https://filters.adtidy.org/ios/filters/224_optimized.txt)  
316. [xinggsf (ios)](https://filters.adtidy.org/ios/filters/228_optimized.txt)  
317. [Fanboy's Anti-thirdparty Fonts (ios)](https://filters.adtidy.org/ios/filters/239_optimized.txt)  
318. [BarbBlock (ios)](https://filters.adtidy.org/ios/filters/240_optimized.txt)  
319. [EasyList Cookie List (ios)](https://filters.adtidy.org/ios/filters/241_optimized.txt)  
320. [NoCoin Filter List (ios)](https://filters.adtidy.org/ios/filters/242_optimized.txt)  
321. [Dandelion Sprout's Annoyances List (ios)](https://filters.adtidy.org/ios/filters/250_optimized.txt)  
322. [Legitimate URL Shortener (ios)](https://filters.adtidy.org/ios/filters/251_optimized.txt)  
323. [Phishing URL Blocklist (ios)](https://filters.adtidy.org/ios/filters/255_optimized.txt)  
324. [Scam Blocklist (ios)](https://filters.adtidy.org/ios/filters/256_optimized.txt)  
325. [uBlock Origin – Badware risks (ios)](https://filters.adtidy.org/ios/filters/257_optimized.txt)  
326. [EasyList](https://easylist.to/easylist/easylist.txt)  
327. [EasyList-adservers](https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_adservers.txt)  
328. [EasyList-thirdparty_servers](https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_thirdparty.txt)  
329. [EasyList-adservers_popup](https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_adservers_popup.txt)  
330. [EasyList-thirdparty_popup](https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_thirdparty_popup.txt)  
331. [EasyList-allowlist](https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_allowlist.txt)  
332. [EasyList-allowlist_dimensions](https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_allowlist_dimensions.txt)  
333. [EasyList-allowlist_general_hide](https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_allowlist_general_hide.txt)  
334. [EasyList-allowlist_popup](https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_allowlist_popup.txt)  
335. [Easylist-general_block](https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_general_block.txt)  
336. [Easylist-general_block_popup](https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_general_block_popup.txt)  
337. [Easylist-general_hide](https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_general_hide.txt)  
338. [EasyPrivacy](https://easylist.to/easylist/easyprivacy.txt)  
339. [EasyPrivacy-allowlist](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_allowlist.txt)  
340. [EasyPrivacy-allowlist_international](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_allowlist_international.txt)  
341. [EasyPrivacy-general](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_general.txt)  
342. [EasyPrivacy-general_emailtrackers](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_general_emailtrackers.txt)  
343. [EasyPrivacy-third-party](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_thirdparty.txt)  
344. [EasyPrivacy-third-party international](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_thirdparty_international.txt)  
345. [EasyPrivacy-trackingservers](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_trackingservers.txt)  
346. [EasyPrivacy-trackingservers_thirdparty](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_trackingservers_thirdparty.txt)  
347. [EasyPrivacy-trackingservers_admiral](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_trackingservers_admiral.txt)  
348. [EasyPrivacy-trackingservers_general](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_trackingservers_general.txt)  
349. [EasyPrivacy-trackingservers_mining](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_trackingservers_mining.txt)  
350. [EasyPrivacy-trackingservers_notifications](https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_trackingservers_notifications.txt) 
351. [Easylist Cookie List](https://secure.fanboy.co.nz/fanboy-cookiemonster.txt)  
352. [Easylist Cookie-allowlist](https://raw.githubusercontent.com/easylist/easylist/master/easylist_cookie/easylist_cookie_allowlist.txt)  
353. [Easylist Cookie-allowlist_general_hide](https://raw.githubusercontent.com/easylist/easylist/master/easylist_cookie/easylist_cookie_allowlist_general_hide.txt)  
354. [Easylist Cookie-general_block](https://raw.githubusercontent.com/easylist/easylist/master/easylist_cookie/easylist_cookie_general_block.txt)  
355. [Easylist Cookie-general_hide](https://raw.githubusercontent.com/easylist/easylist/master/easylist_cookie/easylist_cookie_general_hide.txt)  
356. [Easylist Cookie-thirdparty](https://raw.githubusercontent.com/easylist/easylist/master/easylist_cookie/easylist_cookie_thirdparty.txt)  
357. [EasyList China](https://raw.githubusercontent.com/easylist/easylistchina/master/easylistchina.txt)  
358. [EasyList Adblock Warning Removal List](https://easylist-downloads.adblockplus.org/antiadblockfilters.txt)  
359. [Easylist ABP filters](https://easylist-msie.adblockplus.org/abp-filters-anti-cv.txt)  
360. [Fanboy's Annoyance List](https://secure.fanboy.co.nz/fanboy-annoyance.txt)  
361. [Fanboy's Social Blocking List](https://easylist.to/easylist/fanboy-social.txt)  
362. [Fanboy's Anti-thirdparty Fonts](https://www.fanboy.co.nz/fanboy-antifonts.txt)  
363. [Brave-specific filter](https://raw.githubusercontent.com/brave/adblock-lists/master/brave-lists/brave-specific.txt)  
364. [Brave-ios-specific filter](https://raw.githubusercontent.com/brave/adblock-lists/master/brave-lists/brave-ios-specific.txt)  
365. [Brave-Android-specific filter](https://raw.githubusercontent.com/brave/adblock-lists/master/brave-lists/brave-android-specific.txt)  
366. [Brave-Firstparty filter](https://raw.githubusercontent.com/brave/adblock-lists/master/brave-lists/brave-firstparty.txt)  
367. [Brave-Firstparty-cname filter](https://raw.githubusercontent.com/brave/adblock-lists/master/brave-lists/brave-firstparty-cname.txt)  
368. [Brave-Unbreak filter](https://raw.githubusercontent.com/brave/adblock-lists/master/brave-unbreak.txt)  
369. [The Block List Project - Smart TV List](https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/smart-tv-ags.txt)  
370. [The Block List Project - Ads List](https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/ads-ags.txt)  
371. [The Block List Project - Basic Starter List](https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/basic-ags.txt)  
372. [The Block List Project - Tracking List](https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/tracking-ags.txt)  
373. [The Block List Project - Malware List](https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/malware-ags.txt)  
374. [The Block List Project - Scam List](https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/scam-ags.txt)  
375. [The Block List Project - Phishing List](https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/phishing-ags.txt)  
376. [The Block List Project - Ransomware List](https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/ransomware-ags.txt)  
377. [The Block List Project - Fraud List](https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/fraud-ags.txt)  
378. [The Block List Project - Abuse List](https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/abuse-ags.txt)  
379. [The Block List Project - Redirect List](https://raw.githubusercontent.com/blocklistproject/Lists/master/adguard/redirect-ags.txt)  
380. [Phishing URL Blocklist——ADguard](https://malware-filter.gitlab.io/malware-filter/phishing-filter-ag.txt)  
381. [Phishing URL Blocklist——ADguard Home](https://malware-filter.gitlab.io/malware-filter/phishing-filter-agh.txt)  
382. [Phishing URL Blocklist——uBlock Origin](https://malware-filter.gitlab.io/malware-filter/phishing-filter.txt)  
383. [Malicious URL Blocklist——ADguard](https://malware-filter.gitlab.io/malware-filter/urlhaus-filter-ag.txt)  
384. [Malicious URL Blocklist——ADguard Home](https://malware-filter.gitlab.io/malware-filter/urlhaus-filter-agh.txt)  
385. [Malicious URL Blocklist——uBlock Origin](https://malware-filter.gitlab.io/malware-filter/urlhaus-filter.txt)  
386. [Botnet IP Blocklist——ADguard](https://malware-filter.gitlab.io/malware-filter/botnet-filter-ag.txt)  
387. [Botnet IP Blocklist——ADguard Home](https://malware-filter.gitlab.io/malware-filter/botnet-filter-agh.txt)  
388. [Botnet IP Blocklist——uBlock Origin](https://malware-filter.gitlab.io/malware-filter/botnet-filter.txt)  
389. [Tracking JS Blocklist](https://malware-filter.gitlab.io/malware-filter/tracking-filter.txt)  
390. [abp-filters-anti-cv (English)](https://gitlab.com/eyeo/anti-cv/abp-filters-anti-cv/-/raw/master/english.txt)  
391. [abp-filters-anti-cv (Chinese)](https://gitlab.com/eyeo/anti-cv/abp-filters-anti-cv/-/raw/master/chinese.txt)  
392. [phishing_army_blocklist](https://phishing.army/download/phishing_army_blocklist.txt)  
393. [phishing_army_blocklist_extended](https://phishing.army/download/phishing_army_blocklist_extended.txt)  
394. [OISD Small List](https://small.oisd.nl)  
395. [OISD Big List](https://big.oisd.nl)  
396. [CJX's Annoyance List](https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjx-annoyance.txt)  
397. [CJX's EasyList Lite](https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjxlist.txt)  
398. [CJX's uBlock list](https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjx-ublock.txt)  
399. [AWAvenue-Ads-Rule](https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt)  
400. [AWAvenue-Ads-Rule (Adguard)](https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/Filters/AWAvenue-Ads-Rule-Adguard.txt)  
401. [AWAvenue-Ads-Rule (Adblock)](https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/Filters/AWAvenue-Ads-Rule-Adblock.txt)  
402. [AWAvenue-Ads-Rule (Host)](https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/refs/heads/main/Filters/AWAvenue-Ads-Rule-hosts.txt)  
403. [xinggsf's rules](https://raw.githubusercontent.com/xinggsf/Adblock-Plus-Rule/master/rule.txt)  
404. [xinggsf's mv rules](https://raw.githubusercontent.com/xinggsf/Adblock-Plus-Rule/master/mv.txt)  
405. [HaGeZi's Pro DNS Blocklist](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/pro.txt)  
406. [HaGeZi's Fake DNS Blocklist](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/fake.txt)  
407. [HaGeZi's Light DNS Blocklist](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/light.txt)  
408. [HaGeZi's DynDNS Blocklist](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/dyndns.txt)  
409. [HaGeZi's Normal DNS Blocklist](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/multi.txt)  
410. [HaGeZi's Personal DNS Blocklist](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/personal.txt)  
411. [HaGeZi's Pop-Up Ads DNS Blocklist](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/popupads.txt)  
412. [HaGeZi's Ultimate DNS Blocklist](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/ultimate.txt)  
413. [HaGeZi's The World's Most Abused TLDs - Aggressive](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/spam-tlds-adblock-aggressive.txt)  
414. [HaGeZi's The World's Most Abused TLDs - Allow](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/spam-tlds-adblock-allow.txt)  
415. [HaGeZi's Threat Intelligence Feeds DNS Blocklist](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/tif.txt)  
416. [HaGeZi's Allowlist Referral](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/whitelist-referral.txt)  
417. [HaGeZi's Allowlist URL Shortener](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/whitelist-urlshortener.txt)  
418. [RPiList phishing-Angriffe](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Phishing-Angriffe)  
419. [RPiList malware](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/malware)  
420. [RPiList spam mails](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/spam.mails)  
421. [WindowsSpyBlocker spy](https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt)  
422. [WindowsSpyBlocker spy-v6](https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy_v6.txt)  
423. [WindowsSpyBlocker spy-extra](https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/extra.txt)  
424. [WindowsSpyBlocker spy-extra-v6](https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/extra_v6.txt)  
425. [WindowsSpyBlocker update rules](https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/update.txt)  
426. [WindowsSpyBlocker update IPv6 rules](https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/update_v6.txt)  
427. [Spam404's Adblock-list](https://raw.githubusercontent.com/Spam404/lists/master/adblock-list.txt)  
428. [Spam404's main-blacklist](https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt)  
429. [Scam Blocklist (Adblock Plus)](https://raw.githubusercontent.com/durablenapkin/scamblocklist/master/adguard.txt)  
430. [Scam Blocklist (host)](https://raw.githubusercontent.com/durablenapkin/scamblocklist/master/hosts.txt)  
431. [nocoin-list (adblock)](https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/nocoin.txt)  
432. [nocoin-list (host)](https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt)  
433. [nocoin-list (ublock)](https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/nocoin-ublock.txt)  
434. [Dandelion Sprout's Legitimate URL Shortener](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/LegitimateURLShortener.txt)  
435. [Dandelion Sprout's Anti-Malware List (for ADguard)](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareAdGuard.txt)  
436. [Dandelion Sprout's Anti-Malware List (for Adblock Plus and AdBlock)](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareABP.txt)  
437. [Dandelion Sprout's Anti-Malware List (for AdGuardHome)](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareAdGuardHome.txt)  
438. [Dandelion Sprout's Notifications Blocking List](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Other%20domains%20versions/FanboyNotifications-LoadableInUBO.txt)  
439. [Dandelion Sprout's Compilation List](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AdGuard%20Home%20Compilation%20List/AdGuardHomeCompilationList.txt)  
440. [DanPollock_hosts](https://someonewhocares.org/hosts/hosts)  
441. [DanPollock_hosts_ipv6](https://someonewhocares.org/hosts/ipv6/hosts)  
442. [yokoffing's Annoyance List](https://raw.githubusercontent.com/yokoffing/filterlists/main/annoyance_list.txt)  
443. [yokoffing's Privacy Essentials](https://raw.githubusercontent.com/yokoffing/filterlists/main/privacy_essentials.txt)  
444. [yokoffing's Block third party fonts](https://raw.githubusercontent.com/yokoffing/filterlists/refs/heads/main/block_third_party_fonts.txt)  
445. [yokoffing's clean_reading_experience](https://raw.githubusercontent.com/yokoffing/filterlists/refs/heads/main/clean_reading_experience.txt)  
446. [yokoffing's click2load filters](https://raw.githubusercontent.com/yokoffing/filterlists/refs/heads/main/click2load.txt)  
447. [d3host](https://raw.githubusercontent.com/d3ward/toolz/master/src/d3host.txt)  
448. [d3host-adblock](https://raw.githubusercontent.com/d3ward/toolz/master/src/d3host.adblock)  
449. [Smart-TV Blocklist](https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/refs/heads/master/SmartTV.txt)  
450. [Smart-TV Blocklist for ADguard Home](https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV-AGH.txt)  
451. [Mvps'host](https://winhelp2002.mvps.org/hosts.txt)  
452. [neodevpro's adblock list](https://raw.githubusercontent.com/neodevpro/neodevhost/master/adblocker)  
453. [Peter Lowe’s Ad and Tracking Server List](https://pgl.yoyo.org/adservers/serverlist.php?hostformat=adblockplus&showintro=0)  
454. [Steven Black's ad-hoc list](https://raw.githubusercontent.com/StevenBlack/hosts/master/data/StevenBlack/hosts)  
455. [Anti-Adblock Killer](https://raw.githubusercontent.com/reek/anti-adblock-killer/master/anti-adblock-killer-filters.txt)


</details>

## 五、特别致谢

<details>
  <summary>致谢名单</summary>

1. [Adguard](https://github.com/AdguardTeam/AdGuardFilters)
2. [easylist](https://github.com/easylist/easylist)
3. [uBlockOrigin](https://github.com/uBlockOrigin/uAssets)
4. [Adblocker](https://adblockultimate.net/filters)
5. [Adaway](https://github.com/AdAway/AdAway)
6. [URLhaus](https://urlhaus.abuse.ch)
7. [brave](https://github.com/brave/adblock-lists)
8. [blocklist project](https://github.com/blocklistproject/Lists)
9. [malware-filter](https://gitlab.com/malware-filter)
10. [abp-filters](https://gitlab.com/eyeo/anti-cv/abp-filters-anti-cv)
11. [phishing army](https://www.phishing.army)
12. [oisd](https://github.com/sjhgvr/oisd)
13. [cjxlist](https://github.com/cjx82630/cjxlist)
14. [AWAvenue](https://github.com/TG-Twilight/AWAvenue-Ads-Rule)
15. [xinggsf](https://github.com/xinggsf/Adblock-Plus-Rule)
16. [hagezi](https://github.com/hagezi/dns-blocklists)
17. [StevenBlack](https://github.com/StevenBlack/hosts)
18. [RPiList](https://github.com/RPiList/specials)
19. [WindowsSpyBlocker](https://github.com/crazy-max/WindowsSpyBlocker)
20. [spam404](https://github.com/Spam404/lists)
21. [scamblocklist](https://github.com/durablenapkin/scamblocklist)
22. [nocoin](https://github.com/hoshsadiq/adblock-nocoin-list)
23. [neodevhost](https://github.com/neodevpro/neodevhost)
24. [DandelionSprout](https://github.com/DandelionSprout/adfilt)
25. [DanPollock](https://someonewhocares.org)
26. [yokoffing](https://github.com/yokoffing/filterlists)
27. [Peter Lowe](https://pgl.yoyo.org)
28. [d3ward](https://github.com/d3ward/toolz)
29. [Smart-TV](https://github.com/Perflyst/PiHoleBlocklist)
30. [Mvps](https://winhelp2002.mvps.org)
31. [anti-adblock-killer](https://github.com/reek/anti-adblock-killer)

</details>


<br>
<br>


## LICENSE
- [CC-BY-NC-SA 4.0 License](https://github.com/REIJI007/Adblock-Rule-Collection/blob/main/LICENSE-CC-BY-NC-SA%204.0)
- [GPL-3.0 License](https://github.com/REIJI007/Adblock-Rule-Collection/blob/main/LICENSE-GPL%203.0)
