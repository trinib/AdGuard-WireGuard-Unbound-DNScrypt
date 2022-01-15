<h1 align="center"><b>Disable IPv6 if you don't have it or don't want it. In result if you have weak internet, disabling IPv6 can speed up dns request but have less security.
</b> </h1>

**1.**  In AdGuard homepage go to DNS settings, under DNS server configuration section check `Disable IPv6` option
#

**2.**  Open to unbound config file :
       
    sudo nano /etc/unbound/unbound.conf.d/unbound.conf
       
* Go to line 18 and set `do-ip6: yes` to  `do-ip6: no`
 
#

**2.**  Open to stubby config file :

    cd /etc/stubby/ && sudo rm stubby.yml && sudo nano stubby.yml
    
* comment the lines 246 to 249

#

**4.**  Open cloudflared config file:

    sudo nano /etc/default/cloudflared
        
* Delete `--upstream https://2606:4700:4700::1111/dns-query --upstream https://2606:4700:4700::1001/dns-query`
#

**5.**  Go to https://www.dynu.com/en-US/ControlPanel/DDNS and select _Manage your hostname_(pencil under actions) and *turn off* `Wildcard IPv6 Alias` & `Enable IPv6 Address`
#

### *** _Reboot pi_ ***
