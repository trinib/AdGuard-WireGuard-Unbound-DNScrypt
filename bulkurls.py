from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import ssl
import requests
import json

# +++ A SCRIPT TO ADD MULTIPLE BLOCKLIST AT ONCE IN ADGUARD +++ #

############ INSTRUCTIONS ############

### INSTALL PIP ###
# sudo apt-get install python3-pip -y

### RUN SCRIPT ###
# sudo python3 bulkurls.py

### SET IP / USERNAME / PASSWORD USING *YOUR* ADGUARD CREDENTIALS ###
host = "http://your_pi_ip:80" 
# Your user name
userName = "Yours"
# Your password
password = "Yours"
# block list (can add more of your own) 
urls = [
"https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt",
"https://adaway.org/hosts.txt",
"https://someonewhocares.org/hosts/zero/hosts",
"https://raw.githubusercontent.com/DandelionSprout/adfilt/master/GameConsoleAdblockList.txt",
"https://raw.githubusercontent.com/mitchellkrogza/The-Big-List-of-Hacked-Malware-Web-Sites/master/hosts",
"https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV-AGH.txt",
"https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt",
"https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt",
"https://pgl.yoyo.org/adservers/serverlist.php?hostformat=adblockplus&showintro=1&mimetype=plaintext",
"https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt",
"https://raw.githubusercontent.com/durablenapkin/scamblocklist/master/adguard.txt",
"https://curben.gitlab.io/malware-filter/urlhaus-filter-agh-online.txt",
"https://paulgb.github.io/BarbBlock/blacklists/hosts-file.txt",
"https://abp.oisd.nl/",
"https://v.firebog.net/hosts/Easyprivacy.txt",
"https://v.firebog.net/hosts/Prigent-Ads.txt",
"https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-blocklist.txt",
"https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.2o7Net/hosts",
"https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/KADhosts.txt",
"https://v.firebog.net/hosts/static/w3kbl.txt",
"https://v.firebog.net/hosts/AdguardDNS.txt",
"https://v.firebog.net/hosts/Admiral.txt",
"https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt",
"https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt",
"https://v.firebog.net/hosts/Easylist.txt",
"https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=0&mimetype=plaintext",
"https://raw.githubusercontent.com/bigdargon/hostsVN/master/hosts",
"https://raw.githubusercontent.com/Kees1958/W3C_annual_most_used_survey_blocklist/master/TOP_EU_US_Ads_Trackers_HOST",
"https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt",
"https://osint.digitalside.it/Threat-Intel/lists/latestdomains.txt",
"https://s3.amazonaws.com/lists.disconnect.me/simple_malvertising.txt",
"https://v.firebog.net/hosts/Prigent-Crypto.txt",
"https://bitbucket.org/ethanr/dns-blacklists/raw/8575c9f96e5b4a1308f2f12394abd86d0927a4a0/bad_lists/Mandiant_APT1_Report_Appendix_D.txt",
"https://phishing.army/download/phishing_army_blocklist_extended.txt",
"https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt",
"https://v.firebog.net/hosts/Shalla-mal.txt",
"https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Risk/hosts",
"https://urlhaus.abuse.ch/downloads/hostfile/",
"https://raw.githubusercontent.com/neodevpro/neodevhost/master/lite_host",
"https://raw.githubusercontent.com/neodevpro/neodevhost/master/lite_adblocker",
"https://perflyst.github.io/PiHoleBlocklist/AmazonFireTV.txt",
"https://perflyst.github.io/PiHoleBlocklist/android-tracking.txt",
"https://perflyst.github.io/PiHoleBlocklist/regex.list",
"https://perflyst.github.io/PiHoleBlocklist/SessionReplay.txt",
"https://blocklistproject.github.io/Lists/phishing.txt",
"https://blocklistproject.github.io/Lists/tracking.txt",
"https://raw.githubusercontent.com/ftpmorph/ftprivacy/master/blocklists/smartphone-ads-tracking.txt",
"https://raw.githubusercontent.com/CleanMachine1/AdlistTXTS/main/adservers.txt",
"https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_15_DnsFilter/filter.txt",
"https://easylist-downloads.adblockplus.org/easylist.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_11_Mobile/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_3_Spyware/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_2_English/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_4_Social/filter.txt",
"https://easylist.to/easylist/easyprivacy.txt",
"https://easylist.to/easylist/fanboy-annoyance.txt",
"https://easylist.to/easylist/fanboy-social.txt",
"https://anti-ad.net/easylist.txt",
"https://hosts.anudeep.me/mirror/adservers.txt",
"https://raw.githubusercontent.com/ookangzheng/dbl-oisd-nl/master/abp_light.txt",
"https://raw.githubusercontent.com/ookangzheng/dbl-oisd-nl/master/dbl_light.txt",
"https://raw.githubusercontent.com/ookangzheng/dbl-oisd-nl/master/hosts_light.txt",
"https://raw.githubusercontent.com/ookangzheng/dbl-oisd-nl/master/dnsmasq_light.txt",
"https://raw.githubusercontent.com/ookangzheng/dbl-oisd-nl/master/rpz_basic.rpz",
"https://raw.githubusercontent.com/smed79/blacklist/master/hosts.txt",
"https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt",
"https://raw.githubusercontent.com/azet12/KADhosts/master/KADhosts.txt",
"https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/phishing-domains-ACTIVE.txt",
"https://gitlab.com/quidsup/notrack-blocklists/-/raw/master/malware.list",
"https://gitlab.com/quidsup/notrack-blocklists/-/raw/master/trackers.list",
"https://raw.githubusercontent.com/yous/YousList/master/hosts.txt",
"https://zerodot1.gitlab.io/CoinBlockerLists/list.txt",
"https://gitlab.com/ZeroDot1/CoinBlockerLists/-/raw/master/list_browser.txt",
"https://raw.githubusercontent.com/mitchellkrogza/Badd-Boyz-Hosts/master/domains",
"https://easylist-downloads.adblockplus.org/easyprivacy.txt",
"https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-easylist.txt",
"https://www.i-dont-care-about-cookies.eu/abp/",
"https://hblock.molinero.dev/hosts",
"http://winhelp2002.mvps.org/hosts.txt",
"https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",
"https://raw.githubusercontent.com/VeleSila/yhosts/master/hosts.txt",
"https://iplists.firehol.org/files/alienvault_reputation.ipset",
"https://orca.pet/notonmyshift/domains.txt",
"https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/firewall/spy.txt",
"https://raw.githubusercontent.com/d43m0nhLInt3r/socialblocklists/master/Windows/windowstelemetryblocklist.txt",
"https://raw.githubusercontent.com/d43m0nhLInt3r/socialblocklists/master/MobileAppAds/appadsblocklist.txt",
"https://raw.githubusercontent.com/d43m0nhLInt3r/socialblocklists/master/Android/androidblocklist.txt",
"https://raw.githubusercontent.com/twcau/AdblockRules/master/MurdochList",
"https://raw.githubusercontent.com/twcau/AdblockRules/master/MurdochList",
"https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews/hosts",
"https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/gambling/hosts",
"https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Dead/hosts",
"https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Spam/hosts",
"https://raw.githubusercontent.com/mitchellkrogza/Badd-Boyz-Hosts/master/hosts",
"https://winhelp2002.mvps.org/hosts.txt",
"https://raw.githubusercontent.com/notracking/hosts-blocklists/master/adblock/adblock.txt",
"https://www.github.developerdan.com/hosts/lists/amp-hosts-extended.txt",
"https://raw.githubusercontent.com/badmojr/1Hosts/master/mini/unbound.conf",
"https://raw.githubusercontent.com/badmojr/1Hosts/master/mini/hosts.txt",
"https://raw.githubusercontent.com/badmojr/1Hosts/master/mini/adblock.txt",
"https://raw.githubusercontent.com/badmojr/1Hosts/master/mini/hosts.win",
"https://blocklistproject.github.io/Lists/adguard/ransomware-ags.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt",
"https://curben.gitlab.io/malware-filter/urlhaus-filter.txt",
"https://abp.oisd.nl/basic/",
"https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareAdGuardHome.txt",
"https://curben.gitlab.io/malware-filter/urlhaus-filter-ag.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_general.txt",
"https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
"https://easylist-downloads.adblockplus.org/easyprivacy+easylist.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2022.txt",
"https://secure.fanboy.co.nz/fanboy-annoyance.txt",
"https://easylist.to/easylist/easylist.txt",
"https://curbengh.github.io/malware-filter/urlhaus-filter.txt",
"https://curben.gitlab.io/malware-filter/urlhaus-filter-vivaldi.txt",
"https://curben.gitlab.io/malware-filter/urlhaus-filter-domains.txt",
"https://curben.gitlab.io/malware-filter/urlhaus-filter-agh.txt",
"https://curben.gitlab.io/malware-filter/urlhaus-filter-hosts.txt",
"https://raw.githubusercontent.com/uBlock-LLC/uBlock/master/assets/thirdparties/easylist-downloads.adblockplus.org/easyprivacy.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_adservers.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_general_block.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_adservers_popup.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_trackingservers.txt",
"https://raw.githubusercontent.com/angad/webPriority/master/easylist/easylist/easylist_general_block.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/thirdparties/easylist-downloads.adblockplus.org/easylist.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/thirdparties/easylist-downloads.adblockplus.org/easyprivacy.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2021.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2020.txt",
"https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_thirdparty.txt",
"https://pgl.yoyo.org/adservers/serverlist.php?hostformat=adblock&showintro=0&mimetype=plaintext",
"https://pgl.yoyo.org/adservers/serverlist.php?hostformat=littlesnitch&showintro=0&mimetype=plaintext",
"https://pgl.yoyo.org/adservers/serverlist.php?hostformat=junkbuster&showintro=0&mimetype=plaintext",
"https://pgl.yoyo.org/adservers/serverlist.php?hostformat=unbound&showintro=0&mimetype=plaintext",
"https://pgl.yoyo.org/adservers/serverlist.php?hostformat=iptables&showintro=0&mimetype=plaintext",
"https://pgl.yoyo.org/adservers/serverlist.php?hostformat=msfilter&showintro=0&mimetype=plaintext",
"https://pgl.yoyo.org/adservers/serverlist.php?hostformat=operafilter&showintro=0&mimetype=plaintext",
"https://pgl.yoyo.org/adservers/serverlist.php?hostformat=machosts&showintro=0&mimetype=plaintext
]

############ End Of Edits #################

# Open TLSv1 Adapter
class MyAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=ssl.PROTOCOL_TLSv1)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}     

s = requests.Session()
s.mount(host, MyAdapter())
x = s.post(host + "/control/login", json.dumps({"name": userName, "password" : password}), headers=headers )
print(x.text)

for u in urls:
	filterObj = json.dumps({'url':u, "name":u,"whitelist":False})
	print(filterObj)
	x = s.post(host + "/control/filtering/add_url", data = filterObj, headers=headers)
	print(x.text)
