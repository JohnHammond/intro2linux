#!/bin/bash

function submit_flag(){

	# THE CURL COMMAND FOR THIS WILL VARY
	# SINCE THE uuid OF THE USER WILL BE GENERATED
	# BY THE SERVER
	curl -k "http://localhost:444/submit" --data "uuid=9644903a-bab2-4eb9-b0b3-d83c7a65c305&flag=$1"

}

function clone_repo(){
	git clone "https://github.com/JohnHammond/scripting_playground"
	cd scripting_playground
}

function submit_commit_hashes(){
	git rev-list --remotes | while read line
	do
		submit_flag $line
	done
}

function submit_all_programs(){

	git rev-list --remotes | while read line
	do
		git checkout $line > /dev/null 2>&1
		program_name=`ls | grep -v README.md`
		./$program_name

	done | while read line
	do
		submit_flag "$line"
	done
}

clone_repo

submit_commit_hashes
submit_all_programs


cd ..
rm -rf scripting_playground

# And you could then loop the submission to get flags every minute..
#while [ 1 ];
#do
#	sleep 60
#done
