#!/bin/bash

clear

function install() {
  if (( $EUID != 0 )); then
      printf "\nThe installation is for the current user only! If you want to install for all users run as root!\n"
      echo "The installation will begin in 10 seconds. Press Ctrl+C to abort!"
      sleep 10
      echo "Installing..."
      {
      cd ~/.local/share/ && mkdir cipher_files && cd cipher_files
      wget https://github.com/coder12341/cipher-files/releases/download/1.0.0/cipher-files_linux_amd64 -O cipher_files
      chmod +x qr-generator
      } &> /dev/null
      echo 'export PATH=~/.local/share/cipher_files:$PATH' >> ~/.bashrc
      exit
  fi
    
  echo "The installation will begin in 10 seconds. Press Ctrl+C to abort!"
  sleep 10
  echo "Installing..."
  {
  cd /bin && wget https://github.com/coder12341/cipher-files/releases/download/1.0.0/cipher-files_linux_amd64 -O cipher_files
  chmod +x cipher_files
  
  } &> /dev/null
  exit
}

function uninstall() {
  echo "Removing..."
  if (( $EUID != 0 )); then
    cd ~/.local/share && rm -r cipher_files
    export PATH=${PATH%:~/.local/share/cipher_files}
    exit
  fi
 cd /bin && rm cipher_files
 exit
  
}


printf "(0)Install\n(1)Uninstall\n:"
read mode

if (( "$mode" == "0" )); then
  install
elif (( "$mode" == "1" )); then
  uninstall
else
  echo "Aborting..."
  exit
fi
