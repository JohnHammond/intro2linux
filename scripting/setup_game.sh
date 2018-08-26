#!/bin/bash
# @Author: John Hammond
# @Date:   2016-10-22 10:59:45
# @Last Modified by:   John Hammond
# @Last Modified time: 2016-10-22 14:20:21

# Optional variables: this should be modified by the commandline arguments
USERNAME=""

REPO_NAME="scripting_playground"
PROGRAM_NAMES="program_names.txt"
COMMIT_HASHES="commit_hashes.txt"

RED=`tput setaf 1`							# code for red console text
GREEN=`tput setaf 2`						# code for green text
NC=`tput sgr0`								# Reset the text color


function display_help() {
	cat <<EOF
usage:
	$0 -u USERNAME
parameters:
	-u
		Your username to log into Github.
	-h
		Display help message
EOF
}

function create_a_new_list_of_program_names(){

	echo "" > $PROGRAM_NAMES
}

function create_new_repository(){

	while [ 1 ]
	do
		echo "$FUNCNAME:$GREEN creating repository $REPO_NAME $NC"
		response=`curl -u "$USERNAME" https://api.github.com/user/repos -d "{\"name\":\"$REPO_NAME\"}"`

		echo $response
		echo $response | grep "Bad credentials" > /dev/null 2>&1
		if  [ $? -eq 0 ]
		then
			echo "$FUNCNAME:$RED bad password for $USERNAME! $NC"
			continue
		fi
		echo $response | grep "already exists" > /dev/null 2>&1
		if  [ $? -eq 0 ]
		then
			echo "$FUNCNAME:$RED The repository already exists! $NC"
			exit -1
		fi

		break
	done

}

function clone_the_new_repository(){

	git clone "https://github.com/$USERNAME/$REPO_NAME"
	cd $REPO_NAME
}

function copy_readme_to_the_new_repository(){

	cp ../game_readme.md README.md
	git add .
	git commit -m "Added original README.md"
}


function commit_new_program(){

	program_name=`head /dev/urandom | md5sum | cut -d " " -f1 | base64`

	echo "$FUNCNAME:$GREEN commiting program $program_name $NC"

	# I get rid of the case so the program name and commit message are not equivalent
	# This way a person could not reverse engineer the flags by just the commit message alone
	commit_label=`echo $program_name | tr [:upper:] [:lower:]`

	cp ../minutehash $program_name
	git add . 
	git commit -m "$commit_label"

	echo -e "$program_name" >> ../$PROGRAM_NAMES

	rm $program_name
}

function get_commit_hashes(){

	git rev-list --all --remotes > ../$COMMIT_HASHES
}

function main(){

	create_a_new_list_of_program_names

	create_new_repository
	clone_the_new_repository
	copy_readme_to_the_new_repository

	for i in {1..300}
	do
		commit_new_program
	done

	get_commit_hashes

	push_changes

	remove_the_local_repository

}

function push_changes(){

	git push
	cd ..
}

function remove_the_local_repository(){

	rm -rf $REPO_NAME
}

# Parse script options
while getopts u:h opt; do

	case $opt in
		u)
			echo "$0: ${GREEN}using github username ${OPTARG}${NC}"
			USERNAME=$OPTARG
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
if [ "$USERNAME" == "" ]; then
	echo "$0: ${RED}you must specify your github username!${NC}"
	display_help
	exit -1
fi

# This makes it so every function has a "pre-declaration" of all the functions
main "$@"