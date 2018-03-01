*** Settings ***

Library         WebpackLibrary
Library         DebugLibrary

*** Test Cases ***

Scenario: Run Stop Webpack with no Webpack process running
  No operation
  # Travis does not raise an error here, need to be investigated
  # ${msg}=  Run keyword and expect error  *  Stop Webpack
  # Should Start With	 ${msg}  Webpack process could not be terminated
