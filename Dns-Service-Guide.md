
<h1 align="center"><b>Creating Dynamic DNS Hostname Service</b></a></h1>

<p align="center">
<b>You can choose any of these websites:</b>
<p align="center">
<a href="https://www.dynu.com/"><img src="https://i.imgur.com/0MUVjFU.png" width=220px height=60px></a>
<p align="center">
<a href="https://freedns.afraid.org/"><img src="https://i.imgur.com/wu29VlI.pngg" width=220px height=60px></a>

***I'm currently using dynudns (worked the fastest for me***)
#        
# DYNUDNS 

1. Create account at https://www.dynu.com/en-US/ControlPanel/CreateAccount/

2. Go to https://www.dynu.com/en-US/ControlPanel/DDNS/ and select add domain

<p align="center">
 <img src="https://i.imgur.com/3RRTPBF.jpg" width=800px height=550px>

3. Enter any name in host and select a domain in top level options for example : trinibvpn.freeddns.org

<p align="center">
 <img src="https://i.imgur.com/I1wyqim.jpg" width=800px height=500px>

4. We need to install <a href="https://ddclient.net/"><b>DDclient</b></a> to update external **IP** address when it changes:
           
       sudo apt-get install ddclient -y
 
_It will take you to a setup screen, keep pressing enter until installation is done._
       
5. Put all the parameters in the configuration file before running DDclient:
 
       sudo /usr/sbin/ddclient -daemon 300 -syslog
        
6. Open DDclient configuration file:
    
       sudo nano /etc/ddclient.conf

7. Copy&Paste text below, just change to your username, password, domain name:
     
       # ddclient configuration for Dynu
       #
       # /etc/ddclient.conf
       # Check every 5 minutes
       daemon=600
       # Log update msgs to syslog
       syslog=no
       # Record PID in file
       pid=/var/run/ddclient.pid
       # Get ip from server
       use=web, web=checkip.dynu.com/, web-skip='IP Address'
       # IP update server
       server=api.dynu.com
       protocol=dyndns2
       # Your info
       login=USERNAME
       password=PASSWORD
       DOMAINNAME
      
8. Start DDclient daemon:

       sudo systemctl restart ddclient && sudo systemctl start ddclient
 
**You can reboot router and check in dynu control panel to see if ip updated. _(keep note on the last external ip you had)_**
        
#       
DONE !
#     
# FREEDNS

1. Create account at https://freedns.afraid.org/

2. Click on “Add a subdomain” on the left and enter any subdomain name and pick any domain, but for destination put `0.0.0.0` so we can see if it updates

<p align="center">
 <img src="https://i.imgur.com/YHZC7J8.jpg">

3. We can create a script to update external **IP** address when it changes:
           
       sudo nano free.sh
       
4. Copy&Paste this line but with your token:
 
       echo url="https://freedns.afraid.org/dynamic/update.php?YOURTOKEN" | curl -k -o /home/pi/free.log -K -
        
 * To get token go to https://freedns.afraid.org/dynamic/ and click `direct url` at the botton.At the end of the link in address bar you will see token
    
 <p align="center">
  <img src="https://i.imgur.com/oR4Icyw.jpg">
        
5. Set permission to the file :
    
       sudo chmod 700 free.sh

6. Run this command to check if freedns updated and go to https://freedns.afraid.org/subdomain/ and check if destination option changed to your external ip
     
       sudo /home/pi/free.sh
      
7. Use a cron job to make the script run every 5 minutes

       crontab -e
        
    Add the following to the bottom of the crontab: 
        
       */5 * * * * sudo /home/pi/free.sh >/dev/null 2>&1
  
#        
DONE !

#### If you want to use DDclient instead to update ip for freedns.afraid.org, copy&paste text below in /etc/ddclient.conf:
        
    daemon=5m
    timeout=10
    syslog=no # log update msgs to syslog
    #mail=root # mail all msgs to root
    #mail-failure=root # mail failed update msgs to root
    pid=/var/run/ddclient.pid # record PID in file.
    ssl=yes # use ssl-support. Works with
    # ssl-library

    use=if, if=eth0
    server=freedns.afraid.org
    protocol=freedns
    login=YOUR FREEDNS LOGIN
    password=YOUR FREEDNS PASSWORD
    your.freedns.domain
