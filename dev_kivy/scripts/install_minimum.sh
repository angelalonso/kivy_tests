#!/bin/bash

PACKS=( dropbox gimp guake inkscape python python-numpy python-scipy libreoffice vim virtualbox vlc )

# TODO Confirmation of the process, "Press Y/N to proceed"

echo "Updating package list..." 
sudo apt-get update

echo "Installing the basic packages..." 
for PACK in ${PACKS[@]}
do
	echo -n "Checking if "$PACK" is installed..."
	RES=`dpkg -s $PACK 2>/dev/null | grep "Status" | grep "install ok installed" `
	if [[ $RES == "" ]]; then
		echo " --- Not installed ---"
	        sudo apt-get install $PACK	
	else
		echo " already installed"
	fi

done

