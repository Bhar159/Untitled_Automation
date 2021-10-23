Feature: EuvantageUI Login

  @Positive_testcase
  Scenario: Validate to make sure that registered user able to see the report usage till date
    Given User in Home page
    When User enters username
    And User enters Password
    And User enters the home page login button
    Then User should be logged in successfully
    When User clicks on home and navigate to report-usage till date
    Then File should download


  @Negative_testcase
  Scenario Outline: Registered user comes to application page
    Given User in login page
    When Enter username "<username>" and password "<password>"
    And User enters the login button
    Then User should be logged in home page successfully
    Examples:
      | username  | password  |
      | vikkrams  | pass@123  |
      | vikkrams123 | pass@123  |
