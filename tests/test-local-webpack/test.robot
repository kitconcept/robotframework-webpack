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
  Wait until page contains  Hello World
  Page Should Contain  Hello World


*** Keywords ***

Start Webpack and Open Browser
  Start Webpack  ${HOST}  ${PORT}  path=tests/test-basic  webpack_bin_path=node_modules/webpack-dev-server/bin/webpack-dev-server.js  debug=True
  Open Browser  ${SERVER}  ${BROWSER}
  Set Window Size  1280  1024

Stop Webpack and Close Browser
  Stop Webpack
  Close Browser
