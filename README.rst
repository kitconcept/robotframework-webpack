==============================================================================
A Robot Framework library for Webpack.
==============================================================================

.. image:: https://raw.githubusercontent.com/kitconcept/robotframework-djangolibrary/master/kitconcept.png
   :alt: kitconcept
   :target: https://kitconcept.com/

|br|

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


Documentation
-------------

https://kitconcept.github.io/robotframework-webpack/

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

Rationale
---------

You can start a Webpack process with standard Robot Framework keywords::

  Run process  yarn run build  shell=True  cwd=${CURDIR}
  Run process  yarn global add serve  shell=True  cwd=${CURDIR}
  Start process  serve -s build  shell=True  cwd=${CURDIR}

You can even kill the process at the end of the test (suite)::

  Terminate All Processes  kill=True

Though. You will need to set a sleep statement to wait until the Webpack
process is fully up and running. Since this can take a considerable amount
of time it will make your test suite inefficient and hard to scale.

Robot Framework Webpack checks the output of the Webpack process until it
is fully up and running. As soon as Webpack is ready, the test can continue.


Development
-----------

Project Setup::

  $ virtualenv-2.7 .py27
  $ source .py27/bin/activate
  $ pip install -r requirements.txt
  $ python setup.py develop

Run Tests::

  $ .py27/bin/pybot tests

.. |br| raw:: html

   <br />
