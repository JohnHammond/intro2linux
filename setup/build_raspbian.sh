#!/bin/bash

RASPBIAN_FILENAME="2016-05-27-raspbian-jessie.img"
MICROSD_DEVICE="/dev/mmcblk0"

# Check to see any microSD cards. If you see any, umount them
df -h |grep "$MICROSD_DEVICE"|cut -d " " -f1|while read line; do umount $line; done

# Do we have the IMG file?
if [ -e "$RASPBIAN_FILENAME" ]
then
	# If we do, start to burn it to the MicroSD card.
	dd bs=4M if="$RASPBIAN_FILENAME" of="$MICROSD_DEVICE"
else
	# If not, do we have the zip file?
	if [ -e "${RASPBIAN_FILENAME/.img/.zip}" ]
	then
		# If we do, unzip the zip file.
		unzip "${RASPBIAN_FILENAME/.img/.zip}"
		# If we do, start to burn it to the MicroSD card.
		dd bs=4M if="$RASPBIAN_FILENAME" of="$MICROSD_DEVICE"
	else
		# If not, download the zip file.
		wget "https://downloads.raspberrypi.org/raspbian_latest"
		# unzip it.
		unzip "${RASPBIAN_FILENAME/.img/.zip}"
		# flash the drive
		dd bs=4M if="$RASPBIAN_FILENAME" of="$MICROSD_DEVICE"
	fi

fi


