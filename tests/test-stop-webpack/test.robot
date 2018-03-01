*** Settings ***

Library         WebpackLibrary
Library         DebugLibrary

*** Test Cases ***

Scenario: Run Stop Webpack with no Webpack process running
  ${msg}=  Run keyword and expect error  *  Stop Webpack
  Should Start With	 ${msg}  Webpack process could not be terminated
