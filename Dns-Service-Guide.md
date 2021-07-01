# Creating Dynamic DNS Hostname Service

<p align="center">
<b>You can choose any of these websites:</b>
<p align="center">
<a href="https://www.dynu.com/"><img src="https://i.imgur.com/0MUVjFU.png" width=220px height=60px></a>
<p align="center">
<a href="https://www.duckdns.org/"><img src="https://i.imgur.com/avh2ROy.png" width=220px height=60px></a>
<p align="center">
<a href="https://freedns.afraid.org/"><img src="https://i.imgur.com/wu29VlI.pngg" width=220px height=60px></a>

(I'm currently using dynudns)
#        
# DYNUDNS 

1. Create account at https://www.dynu.com/en-US/ControlPanel/CreateAccount/

2. Go to https://www.dynu.com/en-US/ControlPanel/DDNS/ and select add domain

<p align="center">
 <img src="https://i.imgur.com/3RRTPBF.jpg">

3. Enter any name in host and select a domain in top level options for example : trinibvpn.freeddns.org

<p align="center">
 <img src="https://i.imgur.com/I1wyqim.jpg">

4. We need to create a sh file to update dns service:
           
       sudo nano dynu.sh
       
5. Copy&Paste this line but with your own username and passowrd :
 
       echo url="https://api.dynu.com/nic/update?username=USERNAME&password=PASSWORD" | curl -k -o /home/pi/dynu.log -K -
        
7. Set permission to the file :
    
       sudo chmod 700 dynu.sh

9. Run this command to check if dynudns updated and go back to https://www.dynu.com/en-US/ControlPanel/DDNS/ and under `LAST UPDATED`, you will see time updated
     
       sudo /home/pi/dynu.sh
      
10. Use a cron job to make the script run every 5 minutes

        crontab -e
        
    Add the following to the bottom of the crontab: 
        
        */5 * * * * sudo /home/pi/dynu.sh >/dev/null 2>&1
#       
DONE !
#        
# DUCKDNS

1. Create account at https://www.duckdns.org/

2. Verfy reCAPTCHA and add any domain name

<p align="center">
 <img src="https://i.imgur.com/K8m6Jhf.jpg">

3. We need to make a sh file to update dns service:
           
       sudo nano duck.sh
       
4. Copy&Paste this line but with your own domain name and token :
 
       echo url="https://www.duckdns.org/update?domains=domainname&token=YOURVALUE" | curl -k -o /home/pi/duck.log -K -
        
 * Get token on the site main page
    
<p align="center">
 <img src="https://i.imgur.com/zG47ril.jpg">
        
5. Set permission to the file :
    
       sudo chmod 700 duck.sh

6. Run this command to check if duckdns updated and go to https://www.duckdns.org/ and under `CHANGED`, you will see time updated
     
       sudo /home/pi/duck.sh
      
7. Use a cron job to make the script run every 5 minutes

        crontab -e
        
    Add the following to the bottom of the crontab: 
        
        */5 * * * * sudo /home/pi/duck.sh >/dev/null 2>&1
#        
DONE !
#       
# FREEDNS

1. Create account at https://freedns.afraid.org/

2. Click on “Add a subdomain” on the left and enter any subdomain name and pick any domain, but for destination put `0.0.0.0` so we can see if it updates

<p align="center">
 <img src="https://i.imgur.com/YHZC7J8.jpg">

3. We need to create a sh file to update dns service:
           
       sudo nano free.sh
       
4. Copy&Paste this line but with your token :
 
       echo url="https://freedns.afraid.org/dynamic/update.php?YOURTOKEN" | curl -k -o /home/pi/free.log -K -
        
 * To get token go to https://freedns.afraid.org/dynamic/ and click `direct url` at the botton.At the end of the link in address bar you will see token
    
 <p align="center">
  <img src="https://i.imgur.com/oR4Icyw.jpg">
        
6. Set permission to the file :
    
       sudo chmod 700 free.sh

7. Run this command to check if freedns updated and go to https://freedns.afraid.org/subdomain/ and check if destination option changed to your external ip
     
       sudo /home/pi/free.sh
      
8. Use a cron job to make the script run every 5 minutes

        crontab -e
        
    Add the following to the bottom of the crontab: 
        
        */5 * * * * sudo /home/pi/free.sh >/dev/null 2>&1
#        
DONE !
