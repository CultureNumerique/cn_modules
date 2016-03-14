#!/bin/sh

#

source='build/last'
dest=culturenumerique@culturenumerique.univ-lille3.fr

if [ $# -ge 2 ]; then
    echo "$0 [source]"
    echo "Copy the source dir (default: ./build/last) into the destination $dest " 
    exit 0
else
    if [ $# -eq 1 ]; then
	source=$1
    fi
fi

batchfile=/tmp/synchro-$$
cat <<EOF > $batchfile
cd /site/staging
put -r $source
EOF

if [ -d $source ]; then
    sftp -C -b $batchfile $dest
    #rsync -avh --delete $source $dest
else
    echo "Unable to find: " $source
fi

rm $batchfile


