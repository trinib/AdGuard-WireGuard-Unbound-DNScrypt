#!/bin/bash

echo ' ─ Downloading package...'
wget -o '/tmp/AdGuardHome_linux_arm64.tar.gz'\
    'https://static.adguard.com/adguardhome/release/AdGuardHome_linux_arm64.tar.gz'
echo 'SUCCESS'

echo ' ─  Changing directory...'
cd /opt/AdGuardHome
echo 'SUCCESS'

echo ' ─  Stopping AdGuard Home...'
sudo ./AdGuardHome -s stop
echo 'SUCCESS'

echo ' ─  Backing up data...'
mkdir -p /home/pi/my-agh-backup
cp -r ./AdGuardHome.yaml ./data /home/pi/my-agh-backup/
echo '[*] SUCCESS'

echo ' ─  Unpacking AdGuard Home archive...'
tar -C /tmp/ -f /home/pi/AdGuardHome_linux_arm64.tar.gz -x -v -z
echo 'SUCCESS'

echo ' ─  Replacing the old AdGuard Home executable file with the new one....'
sudo cp /tmp/AdGuardHome/AdGuardHome /opt/AdGuardHome/AdGuardHome
echo 'SUCCESS'

echo ' ─  Restarting AdGuard Home....'
sudo ./AdGuardHome -s start
echo 'SUCCESS'
echo
echo '******Done******'