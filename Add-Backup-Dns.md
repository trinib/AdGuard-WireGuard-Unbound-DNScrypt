### You can a backup DNS server alongside Cloudflare. Here is a <a href="https://kb.adguard.com/en/general/dns-providers"><b>list</b></a> of DNS Providers 
#
I personally use <a href="https://www.quad9.net/about"><b>Quad9 DNS</b></a> provider with DoH / DoT / & Malware Blocking.

In Adguard homepage go to setting / DNS settings

In Upstream DNS servers add :

    https://dns.quad9.net/dns-query
    tls://dns.quad9.net

In Bootstrap DNS servers add :

    9.9.9.9
    149.112.112.112
    2620:fe::fe
    2620:fe::fe:9
    
Go to https://browserleaks.com/dns and you should be connected to WoodyNet and Cloudflare servers
