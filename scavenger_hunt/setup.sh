#!/usr/bin/env bash
# Author: John Hammond
# Date: 11JAN2016
# Description:
#   This script should install all the necessary dependencies and generate a self-signing
#   certificate to be used by a CTF server you can run on your own local machine.
#   If you configure your own CTF with a .json file, you can give that to the server
#   script and it will easily spin up a CTF competition for everyone in the local 
#   network.
#

# Optional variables: this should be modified by the commandline arguments
DATABASE=""
CONFIGURATION=""

# Internal variables; do not edit.
DEPENDENCIES="python-pip sqlite3 python-flask python-passlib"
SERVER_FILE="server_base.py"
NEW_SERVER_FILE="server.py"
SCHEMA_FILE="schema.sql"
PRIVATEKEY_FILE='privateKey.key'
CERTIFICATE_FILE='certificate.crt'

CURRENT_USER=`logname`
RED=`tput setaf 1`							# code for red console text
GREEN=`tput setaf 2`						# code for green text
NC=`tput sgr0`								# Reset the text color

function display_help() {
	cat <<EOF
usage:
	$0 -d DATABASE -c CONFIGURATION
parameters:
	-d
		Specify the database file that will be created and used for this server.
		Example: '/tmp/ctf-practice.db'
	-c
		Specify the configuration file that will be used for this server.
		Example: 'ctf_practice.json'
	-h
		Display help message
EOF
}


function install_dependencies(){

	echo "$0: ${GREEN}installing dependenices...${NC}"
	apt-get update || panic
	apt-get -y install $DEPENDENCIES || panic
}

function create_certificate(){

	echo "$0: ${GREEN}creating HTTPS certificates...${NC}"
	# openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout $PRIVATEKEY_FILE -out $CERTIFICATE_FILE || panic
	openssl req -newkey rsa:2048 -nodes -keyout "$PRIVATEKEY_FILE" \
							-x509 -days 365 -out "$CERTIFICATE_FILE" <<EOF || panic
US
CT
New London
United States Coast Guard Academy
Cyber Team
John Hammond
johnhammond010@gmail.com
EOF

	sed "0,/\$CERTIFICATE_FILE/{s/\$CERTIFICATE_FILE/$CERTIFICATE_FILE/}" $SERVER_FILE > $NEW_SERVER_FILE || panic
	sed -i "0,/\$PRIVATEKEY_FILE/{s/\$PRIVATEKEY_FILE/$PRIVATEKEY_FILE/}" $NEW_SERVER_FILE || panic
	

}

function create_database(){

	echo "$0: ${GREEN}creating sqlite3 database...${NC}"

	rm -f $DATABASE
	sqlite3 $DATABASE < $SCHEMA_FILE || panic
	chown $CURRENT_USER $DATABASE
	sed -i '0,/\$DATABASE/{s/\$DATABASE/'${DATABASE//\//\\/}'/}' $NEW_SERVER_FILE  || panic

}

function configure_ctf(){

	echo "$0: ${GREEN}configuring CTF...${NC}"

	sed -i "0,/\$CONFIGURATION/{s/\$CONFIGURATION/$CONFIGURATION/}" $NEW_SERVER_FILE || panic

}

function create_new_server(){

	cp $SERVER_FILE $NEW_SERVER_FILE
	chown $CURRENT_USER $NEW_SERVER_FILE
	chmod 744 $NEW_SERVER_FILE
}

function configure_firewall(){
	
	# Allow incoming connections...
	echo "$0: ${GREEN} Configuring firewall for HTTPS connections...${NC}"
	ufw allow https
}

function main()
{

	install_dependencies

	create_new_server

	create_certificate
	
	create_database

	configure_ctf

	configure_firewall

	echo "$0: ${GREEN} CTF server successfully setup!${NC}"
	echo "$0: ${GREEN} You should now be able to run the server with the command: ${NC}"
	echo '`sudo python server.py`'

	exit 0
	
}

# Print a fatal error message and exit
# Usage:
# 	some_command parameter || panic
# 	
# 	This will print the panic message and exit if `some_command` fails.
function panic
{
	echo "$0: ${RED}fatal error${NC}"
	exit -1
}


# Make sure the user is root (e.g. running as sudo)
if [ "$(id -u)" != "0" ]; then
	echo "$0: ${RED}you must be root to configure this box.${NC}"
	exit -1
fi

# Parse script options
while getopts d:c:h opt; do

	case $opt in
		d)
			echo "$0: ${GREEN}using database file ${OPTARG}${NC}"
			DATABASE=$OPTARG
			;;
		c)
			echo "$0: ${GREEN}using configuration file ${OPTARG}${NC}"
			CONFIGURATION=$OPTARG
			;;
		h)
			display_help
			exit 0
			;;
		\?)
			exit -1
			;;
	esac
done


# Make sure we entered a database name
if [ "$DATABASE" == "" ]; then
	echo "$0: ${RED}you must specify a database file!${NC}"
	display_help
	exit -1
fi

# Make sure we entered a configuration file
if [ "$CONFIGURATION" == "" ]; then
	echo "$0: ${RED}you must specify a configuration file!${NC}"
	display_help
	exit -1
fi

# This makes it so every function has a "pre-declaration" of all the functions
main "$@"