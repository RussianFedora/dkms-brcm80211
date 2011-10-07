#!/bin/sh

NAME=brcm80211
COMMIT="ed6e3facef31a711d010ce6a7bb907e9a9cafabb"

git clone -q git://github.com/elemc/brcm80211.git

pushd ${NAME} > /dev/null 2>&1
git checkout -qf $COMMIT
popd > /dev/null 2>&1

# Remove .git
rm -rf ${NAME}/.git

# make tarboll
tar cfjv ${NAME}.tar.bz2 $NAME > /dev/null 2>&1

# remove dir
rm -rf ${NAME}