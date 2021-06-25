<p align="center">
 <img src="https://i.imgur.com/oNX4y4R.png" width=200px height=200px>
    
<h1 align="center"><b>You can add another DNS server alongside Cloudflare for more strenght. Here is a <a href="https://kb.adguard.com/en/general/dns-providers"><b>list</b></a> of DNS Providers </b> </h1>

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

<p align="center">
 <img src="https://i.imgur.com/S6DAGNB.jpg" width=800px height=500px>
