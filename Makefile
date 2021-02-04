# Makefile for Scaffolder CLI
# usage: make OLD-RELEASE=0.1.4 NEW-RELEASE=0.2.0 all

.PHONY: install build release publish all

install:
	sudo -H pip install scaffolder

build:
	# updates snap/snapcraft.yaml version
	sed -i '' 's/$(OLD-RELEASE)/$(NEW-RELEASE)/g' snap/snapcraft.yaml   
	# updates setup.py version
	edit setup.py and increase version
	sed -i '' 's/$(OLD-RELEASE)/$(NEW-RELEASE)/g' setup.py
	git commit -am "New release $(NEW-RELEASE)"

release:
	gh release create $(NEW-RELEASE) -F CHANGELOG.md
	snapcraft release

publish:
	# push to PyPi
	./build.sh
	# 
	snapcraft login
	snapcraft upload --release=edge cli-$(NEW-RELEASE).snap
	# login to snapcraft.io and check if the build is OK

all: build release publish