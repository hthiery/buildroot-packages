#!/usr/bin/env bash

BASEDIR=$(dirname "$0")

BR_PACKAGES="/var/lib/buildroot-packages"

cd ${BASEDIR}

if [ ! -d buildroot ]; then
	git clone git://git.busybox.net/buildroot
fi

cd buildroot
git pull git://git.busybox.net/buildroot

# create stats.json
support/scripts/pkg-stats --json stats.json --nvd-path /tmp/nvd

cp stats.json ${BR_PACKAGES}

pushd ${BR_PACKAGES}
# first create a new db file
./import import -i stats.json --db new.db

rm br-pkg.db
mv new.db br-pkg.db
popd
