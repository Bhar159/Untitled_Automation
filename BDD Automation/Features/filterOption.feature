Feature: Usage till date page validation(Filter option)

  Background: Common steps in filter scenario
    Given user open the login page
    When user enters user id and password
    And User click the login button
    Then user successfully logged in home page
    When User select home button and navigate to report and usage till_date
    Then User successfully reached Usage till date page
    When User select filter option
    And User enters the Pool name and server name and User name

  @slow
  Scenario: Validate to make sure that search option functioning as excepted
    When User click on search button
    Then User navigated to expected page
  @checking2
  Scenario: Validate that Top search option working as expected
    When User select the value from the drop down
    Then Verify selected value displayed in the report
  @checking3
  Scenario: Validate that slider button option working as expected
    When User drag the slider button
    Then Verify selected value displayed in the report window
  @checking4
   Scenario: Validate that Clear All option working as expected
     When User clicks on clear all button
     Then Verity that text in the pool name,server ip,server name,session ip,username should be removed


