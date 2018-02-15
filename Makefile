SHELL := /bin/bash
CURRENT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

all: clean build test

clean:
	@echo "Clean"
	rm -rf .py27

build:
	@echo "Build"
	virtualenv .py27
	.py27/bin/pip install -r requirements.txt
	.py27/bin/python setup.py develop
	(cd tests/test-basic && npm install)

test:
	@echo "Run Tests"
	.py27/bin/pybot tests

build-docs:
	@echo "Build Keyword Documentation"
	.py27/bin/python -m robot.libdoc WebpackLibrary docs/index.html
