#!/bin/bash
# @Author: John Hammond
# @Date:   2016-08-28 15:08:22
# @Last Modified by:   John Hammond
# @Last Modified time: 2016-08-28 15:31:15


# Colors for good display...
BLACK=`tput setaf 0`
RED=`tput setaf 1`
GREEN=`tput setaf 2`
YELLOW=`tput setaf 3`
BLUE=`tput setaf 6`
RESET=`tput sgr0`


DEPENDENCIES="nodejs-legacy npm"

function install_dependencies(){

	echo "${FUNCNAME}:${GREEN} installing nodejs and npm...${RESET}"

	apt-get -y install $DEPENDENCIES || fatal_error
}

function install_hjson(){

	echo "${FUNCNAME}:${GREEN} installing hjson with npm...${RESET}"
	npm install hjson -g
}

function fatal_error(){

	echo "${FUNCNAME}:${RED} aborting...${RESET}"
	exit -1
}

function main(){

	echo "${BLUE} This script will install the dependencies that you should have"
	echo "${BLUE} to develop for the Training Wheels shell."
	echo -e "${BLUE} It is really just for convenience sake of using HJSON.\n ${RESET}"

	install_dependencies

	install_hjson

}

if [ "$UID" != "0" ]
then
	echo "You must be root to run this script!"
	fatal_error
fi


main $@