#!/bin/bash

executed_flag="false"
install_aborted="false"

### Install Log2ram to reduce the logging impact on the SD Card
### Refer to https://github.com/azlux/log2ram for more details

### Installing 
## wget https://git.io/log2ram -O Log2Ram-Script.sh && sudo chmod +x Log2Ram-Script.sh && sudo ./Log2Ram-Script.sh

#### Uninstalling log2ram (if needed in future)
## sudo chmod +x /usr/local/bin/uninstall-log2ram.sh && sudo /usr/local/bin/uninstall-log2ram.sh

cd $Home
#Confirm internet connectivity
internet_access=$(ping -q -c 1 -W 1 1.1.1.1 > /dev/null 2>&1; echo $?)
log2ram_present=$(log2ram status > /dev/null 2>&1; echo $?)
if [[ ($log2ram_present != 1) && ($internet_access == 0) && ($install_aborted == "false") ]]
then
	#Fetch the Log2RAM from githib
	curl -Lo log2ram.tar.gz https://github.com/azlux/log2ram/archive/master.tar.gz
	tar xf log2ram.tar.gz
	cd log2ram-master
	chmod +x install.sh && sudo ./install.sh
	cd ..
	#Remove files that are no longer required
	rm -r log2ram-master
	rm log2ram.tar.gz
	executed_flag="true"
	echo "$(tput setaf 2)FINISH !!!$(tput sgr0)"
        echo "$(tput setaf 2)$(tput sgr0)"
elif [[ $internet_access -gt 0 ]]
then
	echo "$(tput setaf 1)No internet. Exiting.$(tput sgr0)"
elif [[ $install_aborted == "true" ]]
then
	echo "$(tput setaf 1)Log2Ram installation aborted.$(tput sgr0)"
else
	echo "Log2RAM already installed. Skipping installation."
fi

###Reboot
if [[ $executed_flag == "true" ]]
then
	echo "$(tput setaf 2)Log2Ram installation is complete.$(tput sgr0)$(tput setaf 1) Rebooting.....$(tput sgr0)"

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
RESET='\033[0m'
hour=0
min=0
sec=5
tput civis
echo -ne "${GREEN}"
        while [ $hour -ge 0 ]; do
                 while [ $min -ge 0 ]; do
                         while [ $sec -ge 0 ]; do
                                 if [ "$hour" -eq "0" ] && [ "$min" -eq "0" ]; then
                                         echo -ne "${YELLOW}"
                                 fi
                                 if [ "$hour" -eq "0" ] && [ "$min" -eq "0" ] && [ "$sec" -le "10" ]; then
                                         echo -ne "${RED}"
                                 fi
                                 echo -ne "$(printf "%02d" $hour):$(printf "%02d" $min):$(printf "%02d" $sec)\033[0K\r"
                                 let "sec=sec-1"
                                 sleep 1
                         done
                         sec=59
                         let "min=min-1"
                 done
                 min=59
                 let "hour=hour-1"
         done
echo -e "${RESET}"
tput cnorm
	sudo reboot
else
	echo "No changes done. Exiting."
fi
