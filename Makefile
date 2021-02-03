
.PHONY: install

install:
	sudo -H pip install scaffolder

build:
	edit snap/snapcraft.yaml and increase version
	commit to origin/master
	edit setup.py
release:

publish:
	./build.sh will push to PyPi
	Login to snapcraft.io and trigger manual build

