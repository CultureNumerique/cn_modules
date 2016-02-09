#!/bin/sh

#

source='build'
dest=vduhal@culturenumerique.univ-lille3.fr:htdocs/staging/

if [ $# -ge 2 ]; then
    echo "$0 [source]"
    echo "Copy the source dir (default: build) into the destination $dest " 
    exit 0
else
    if [ $# -eq 1 ]; then
	source=$1
    fi
fi

if [ -d $source ]; then
    scp  -r -C $source $dest
    #rsync -avh --delete $source $dest
else
    echo "Unable to find: " $source
fi
   

