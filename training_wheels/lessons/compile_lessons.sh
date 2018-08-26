#!/bin/bash

ls *.hjson|while read line
do
	hjson -j "$line" > ".${line/hjson/json}"
done

# We should add in a carriage return to all new-lines so we can use
# the curses mode!
ls .*.json|while read line
do
	sed -i 's/\\n/\\n\\r/g' ${line}
done