#!/bin/sh

#rsync -avh --delete build vduhal@culturenumerique.univ-lille3.fr:htdocs/staging
scp  -r build vduhal@culturenumerique.univ-lille3.fr:htdocs/staging

