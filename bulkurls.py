from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import ssl
import requests
import json

# +++ A SCRIPT TO ADD MULTIPLE BLOCKLIST AT ONCE IN ADGUARD +++ #

### RUN SCRIPT ###
# sudo python3 bulkurls.py

### SET IP / USERNAME / PASSWORD USING *YOUR* ADGUARD CREDENTIALS ###
host = "http://your_pi_ip:80" 
# Your user name
userName = "Yours"
# Your password
password = "Yours"

### Example urls (can remove and add your own from https://github.com/T145/black-mirror#-sources) 
urls = [
"https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt",
"https://adaway.org/hosts.txt",
"https://abp.oisd.nl/",
"https://v.firebog.net/hosts/Easyprivacy.txt",
"https://v.firebog.net/hosts/Prigent-Ads.txt",
"https://v.firebog.net/hosts/static/w3kbl.txt",
"https://v.firebog.net/hosts/AdguardDNS.txt",
"https://v.firebog.net/hosts/Admiral.txt",
"https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt",
"https://v.firebog.net/hosts/Easylist.txt",
"https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=0&mimetype=plaintext",
"https://osint.digitalside.it/Threat-Intel/lists/latestdomains.txt",
"https://v.firebog.net/hosts/Prigent-Crypto.txt",
"https://raw.githubusercontent.com/neodevpro/neodevhost/master/lite_host",
"https://raw.githubusercontent.com/neodevpro/neodevhost/master/lite_adblocker",
"https://perflyst.github.io/PiHoleBlocklist/AmazonFireTV.txt",
"https://perflyst.github.io/PiHoleBlocklist/android-tracking.txt",
"https://perflyst.github.io/PiHoleBlocklist/regex.list",
"https://perflyst.github.io/PiHoleBlocklist/SessionReplay.txt",
"https://someonewhocares.org/hosts/zero/hosts",
"https://raw.githubusercontent.com/DandelionSprout/adfilt/master/GameConsoleAdblockList.txt",
"https://raw.githubusercontent.com/mitchellkrogza/The-Big-List-of-Hacked-Malware-Web-Sites/master/hosts",
"https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV-AGH.txt",
"https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt",
"https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt",
"https://pgl.yoyo.org/adservers/serverlist.php?hostformat=adblockplus&showintro=1&mimetype=plaintext",
"https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt",
"https://raw.githubusercontent.com/durablenapkin/scamblocklist/master/adguard.txt",
"https://raw.githubusercontent.com/ftpmorph/ftprivacy/master/blocklists/smartphone-ads-tracking.txt",
"https://raw.githubusercontent.com/CleanMachine1/AdlistTXTS/main/adservers.txt",
"https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt",
"https://easylist-downloads.adblockplus.org/easylist.txt",
"https://easylist.to/easylist/easyprivacy.txt",
"https://easylist.to/easylist/fanboy-annoyance.txt",
"https://easylist.to/easylist/fanboy-social.txt",
"https://anti-ad.net/easylist.txt",
"https://hosts.anudeep.me/mirror/adservers.txt",
"https://raw.githubusercontent.com/ookangzheng/dbl-oisd-nl/master/abp_light.txt",
"https://raw.githubusercontent.com/ookangzheng/dbl-oisd-nl/master/dbl_light.txt",
"https://raw.githubusercontent.com/ookangzheng/dbl-oisd-nl/master/hosts_light.txt",
"https://raw.githubusercontent.com/ookangzheng/dbl-oisd-nl/master/dnsmasq_light.txt",
"https://raw.githubusercontent.com/smed79/blacklist/master/hosts.txt",
"https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt",
"https://raw.githubusercontent.com/azet12/KADhosts/master/KADhosts.txt",
"https://easylist-downloads.adblockplus.org/easyprivacy.txt",
"https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-easylist.txt",
"https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",
"https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews/hosts",
"https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/gambling/hosts",
"https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Dead/hosts",
"https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Spam/hosts",
"https://raw.githubusercontent.com/mitchellkrogza/Badd-Boyz-Hosts/master/hosts",
"https://raw.githubusercontent.com/notracking/hosts-blocklists/master/adblock/adblock.txt",
"https://raw.githubusercontent.com/badmojr/1Hosts/master/mini/hosts.txt",
"https://raw.githubusercontent.com/badmojr/1Hosts/master/mini/adblock.txt",
"https://blocklistproject.github.io/Lists/adguard/ransomware-ags.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt",
"https://abp.oisd.nl/basic/",
"https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareAdGuardHome.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt",
"https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
"https://easylist-downloads.adblockplus.org/easyprivacy+easylist.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2022.txt",
"https://secure.fanboy.co.nz/fanboy-annoyance.txt",
"https://easylist.to/easylist/easylist.txt",
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
"https://pgl.yoyo.org/adservers/serverlist.php?hostformat=adblock&showintro=0&mimetype=plaintext"
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
