SHELL := /bin/bash
CURRENT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

all: clean build test

clean:
	@echo "Clean"
	rm -rf .py27

build:
	@echo "Build"
	virtualenv-2.7 .py27
	.py27/bin/pip install -r requirements.txt
	.py27/bin/python setup.py develop
	(cd tests/test-basic && npm install)
test:
	@echo "Run Tests"
	.py27/bin/pybot tests

test-phantomjs:
	@echo "Run Tests"
	.py27/bin/pybot --variable BROWSER:phantomjs tests
