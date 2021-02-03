
.PHONY: install build release publish

install:
	sudo -H pip install scaffolder

build:
	edit snap/snapcraft.yaml and increase version
	commit to origin/master
	edit setup.py
	
release:
	gh release create $(RELEASE) -F CHANGELOG.md

publish:
	./build.sh will push to PyPi
	Login to snapcraft.io and trigger manual build
