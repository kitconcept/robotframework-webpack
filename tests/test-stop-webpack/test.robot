*** Settings ***

Library         WebpackLibrary
Library         DebugLibrary

*** Test Cases ***

Scenario: Run Stop Webpack with no Webpack process running
  ${msg}=  Run Keyword And Continue On Failure  Stop Webpack
  Should Start With	 ${msg}  Webpack process could not be terminated
