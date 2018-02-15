==============================================================================
A Robot Framework library for Webpack.
==============================================================================

.. image:: https://travis-ci.org/kitconcept/robotframework-webpack.svg?branch=master
    :target: https://travis-ci.org/kitconcept/robotframework-webpack

.. image:: https://img.shields.io/pypi/status/robotframework-webpack.svg
    :target: https://pypi.python.org/pypi/robotframework-webpack/
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/v/robotframework-webpack.svg
    :target: https://pypi.python.org/pypi/robotframework-webpack/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/l/robotframework-webpack.svg
    :target: https://pypi.python.org/pypi/robotframework-webpack/
    :alt: License


Introduction
------------

WebpackLibrary is a Robot Framework library for Webpack. It allows to start
and stop the Webpack dev server.

Installation
------------

Install robotframework-webpack with pip::

  $ pip install robotframework-webpack


Usage
-----

In order to write your first robot test, make sure that you include Selenium2Library and WebpackLibrary. Create a test.robot file with the following content::

  *** Variables ***

  ${HOST}                 127.0.0.1
  ${PORT}                 8080
  ${BROWSER}              chrome
  ${SERVER}               http://${HOST}:${PORT}


  *** Settings ***

  Documentation   WebpackLibrary Acceptance Tests
  Library         Selenium2Library  timeout=10  implicit_wait=0
  Library         WebpackLibrary
  Suite Setup     Start Webpack and Open Browser
  Suite Teardown  Stop Webpack and Close Browser


  *** Test Cases ***

  Scenario: Webpack Dev Server
    Go To  ${SERVER}
    # Amend this line to check for the real content of your app. Otherwise this test will fail.
    Wait until page contains  Hello World
    Page Should Contain  Hello World


  *** Keywords ***

  Start Webpack and Open Browser
    Start Webpack  yarn start
    Open Browser  ${SERVER}  ${BROWSER}
    Set Window Size  1280  1024

  Stop Webpack and Close Browser
    Stop Webpack
    Close Browser


Keywords
--------

Start Webpack: Starts the webpack process. The keyword take the command line command to start Webpack (e.g. 'yarn start').

  Start Webpack  yarn start

Optional parameters are:

  - path: relative or absolute path to the path where the command should be executed.
  - check: string that the keyword looks for in the Webpack output to know that Webpack has been fully started (default is 'Compiled successfully').
  - debug: returns debug information

Example with all parameters set::

  Start Webpack  yarn start
  ..  path=tests/test-create-react-app
  ..  check=Compiled successfully
  ..  debug=True

Stop Webpack: Stopps the webpack process that has been started with 'Start Webpack'.
The keyword has no parameters.

Development
-----------

Project Setup::

  $ virtualenv-2.7 .py27
  $ source .py27/bin/activate
  $ pip install -r requirements.txt
  $ python setup.py develop

Run Test::

  $ pybot test.robot

.. |br| raw:: html

   <br />
