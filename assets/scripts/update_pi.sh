#!/bin/bash

echo '[*] Refreshing repository cache...'
sudo apt-get update -y
echo '[*] Repository cache refreshed.'

echo '[*] Upgrading all existing packages...'
sudo apt-get upgrade -y
echo '[*] Existing packages upgraded.'

echo '[*] Upgrading Linux distribution (if available)...'
sudo apt-get dist-upgrade -y
echo '[*] Linux distribution upgrade processed.'

echo '[*] Clean up unused and cached packages...'
sudo apt-get autoclean -y
sudo apt-get autoremove -y
echo '[*] Package cleanup complete.'

echo "[*] Rebooting..."
sudo reboot
