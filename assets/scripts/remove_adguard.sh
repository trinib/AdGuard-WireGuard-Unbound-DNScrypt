#!/bin/sh

echo '\033[0;91m ─ Changing directory to /opt...\033[0m'
cd /opt/AdGuardHome

echo '\033[0;91m ─ Uninstalling...\033[0m'
sudo ./AdGuardHome -s uninstall

echo '\033[0;91m ─ Deleting folder...\033[0m'
cd /opt/ 
sudo rm -r AdGuardHome
cd

echo '\033[1;34m*****Done*****\033[0m'
