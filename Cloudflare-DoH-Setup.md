<p align="center">
 <img src="https://i.imgur.com/rbdy7w7.png" width=220px height=100px>

#### For 32bit OS
### Download cloudflare ARM 32bit and extract it:
 
Go to https://github.com/cloudflare/cloudflared/releases , right click on `cloudflared-linux-arm` and copy link. In terminal type **"wget copiedlink"** . For example :

    wget https://github.com/cloudflare/cloudflared/releases/download/2021.12.4/cloudflared-linux-arm
 
### Copy the cloudflared file to /usr/local/bin/ and update permissions:
  
    sudo cp cloudflared-linux-arm /usr/local/bin/cloudflared && sudo chmod +x /usr/local/bin/cloudflared
 
Done!
#

#### For 64bit OS
### Download cloudflare ARM 64bit :
 
Go to https://github.com/cloudflare/cloudflared/releases , right click on `cloudflared-linux-arm64` and copy link. In terminal type **"wget copiedlink"** . For example :
 
    wget https://github.com/cloudflare/cloudflared/releases/download/2021.3.0/cloudflared-linux-arm64
 
### Rename and copy the cloudflared file to /usr/local/bin/ and update permissions:
  
    sudo cp cloudflared-linux-arm64 /usr/local/bin/cloudflared && sudo chmod +x /usr/local/bin/cloudflared
  
Done!
#
 
### After installing cloudflare 64bit or 32bit check version:
    
    cloudflared -v
    
<p align="center">
 <img src="https://i.imgur.com/Qe3ho9r.jpg">

### Create user:

    sudo useradd -s /usr/sbin/nologin -r -M cloudflared

### Download and save the cloudflare config file to /etc/default:
    
    cd /etc/default && sudo wget https://raw.githubusercontent.com/trinib/Adguard-Wireguard-Unbound-Cloudflare/main/cloudflared

### Set correct permissions on cloudflare:

    sudo chown cloudflared:cloudflared /etc/default/cloudflared && sudo chown cloudflared:cloudflared /usr/local/bin/cloudflared

### Download the cloudflare service file and save it to /lib/systemd/system:

    cd /lib/systemd/system && sudo wget https://raw.githubusercontent.com/trinib/Adguard-Wireguard-Unbound-Cloudflare/main/cloudflared.service

### Start cloudflare:
    
    sudo systemctl enable cloudflared && sudo systemctl start cloudflared

### Check status:

    sudo systemctl status cloudflared

<p align="center">
 <img src="https://i.imgur.com/DTEPmy1.jpg">
 
 `ctrl + c` to exit status window
#
 
### `IMPORTANT`
The cloudflared tool will not receive updates through the package manager. However, you should keep the program update to date. You can either do this manually, or automatically with cron script.

Open cron file:
 
    crontab -e
 
Paste command at end of file:
  
    0 3 * * FRI sudo cloudflared update && sudo systemctl restart cloudflared
 
 Will run at 3am every Friday.
    
 
