<p align="center">
 <img src="https://i.imgur.com/NHnVeTB.gif" width=300px height=100px>

#
**Before installing Openvpn**, if you do not have a static ip you need to get a free `Dynamic DNS Subdomain` or else your external IP address most likely changes dynamically from your ISP ever so often and for that reason you'll need to set up a dynamic DNS service. 👉👉 **_▓▒░Use this <a href="https://github.com/trinib/Adguard-Wireguard-Unbound-Cloudflare/blob/main/Dns-Service-Guide.md"><b>INSTRUCTION HERE</b></a>░▒▓_** 👈👈. Or else skip the step.


We also need to set up port fowarding on your router so we can access openvpn outside of our network like in a coffee shop hotspot or your mobile data
TYPE | VALUE     
------------ | -------------
Device | Raspberry Pi's hostname or IP
Protocol | UDP
Port range | 1194-1194
Outgoing port | 1194
Permit Internet acces(if have) | yes   
  
#
Install OpenVPN type in terminal:
 
    wget https://git.io/vpn -O openvpn-install.sh && sudo bash openvpn-install.sh
  
* The script is going to ask you for the hostname that you want to use for the VPN. _If_ you have static ip then continue or else type the dynamic DNS domain that you created from the <a href="https://github.com/trinib/Adguard-Wireguard-Unbound-Cloudflare/blob/main/Dns-Service-Guide.md"><b>instructions</b></a>. For example:trinibvpn.freeddns.org

* For protocol option select 1 for `UDP` 
  
* For port option `press enter` for default 1194. For client name, just put any name you want, and for DNS use option 3 (`1.1.1.1`).  
<p align="center">
 <img src="https://i.imgur.com/dNuZR35.jpg">
  
* Wait until the installation is finished, you will see "The client configuration is available in: /root/yourclientname.ovpn"
  
* Then create txt file with any name on pc and copy&paste the text from config client ovpn file. To see text, type in terminal:
  
      sudo cat /root/yourclientname.ovpn
  
* Highlight all the text and paste it in the txt file on pc and save. Then rename the extention from `txt` to `ovpn`. Now you have config file for that OpenVPN client.
  
### ╸ Connecting To The VPN From A PC (Windows) ╸

Wireguard for windows: https://openvpn.net/downloads/openvpn-connect-v3-windows.msi
  
Import the ovpn client file in OpenVPN to connect
  
### ╸ Connecting To The VPN To Android/IOS Phone ╸

OpenVPN (Google Play): https://play.google.com/store/apps/details?id=de.blinkt.openvpn&hl=en&gl=US

OpenVPN (App Store): https://apps.apple.com/us/app/openvpn-connect/id590379981
  
* Copy over the opvn client file you created on pc to your phone and import file in OpenVPN app to connect
#
  
  
