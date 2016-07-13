==============================================================================
A robot framework library for Webpack.
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
  ${PORT}                 7447
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
    Start Webpack  ${HOST}  ${PORT}  debug=False
    Open Browser  ${SERVER}  ${BROWSER}
    Set Window Size  1280  1024

  Stop Webpack and Close Browser
    Stop Webpack
    Close Browser



Development
-----------

Project Setup::

  $ virtualenv-2.7 .py27
  $ source .py27/bin/activate
  $ pip install -r requirements.txt
  $ python setup.py develop

Run Test::

  $ pybot test.robot

