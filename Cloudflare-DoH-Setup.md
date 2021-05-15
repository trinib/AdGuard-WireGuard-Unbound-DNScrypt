<p align="center">
 <img src="https://i.imgur.com/rbdy7w7.png" width=220px height=100px>

### Download cloudflare and extract it:

    wget https://bin.equinox.io/c/VdrWdbjqyF/cloudflared-stable-linux-arm.tgz && tar -xvzf cloudflared-stable-linux-arm.tgz

### Copy the cloudflare folder to /usr/local/bin/ and update permissions:
  
    sudo cp cloudflared /usr/local/bin/ && sudo chmod +x /usr/local/bin/cloudflared

Check Version:
    
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
 <img src="https://i.imgur.com/VNGjqIu.jpg">
