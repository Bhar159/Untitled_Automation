Feature: Functionality to check (Daily Healthcheck)

  Background: Common steps in Health check scenario
    Given user in the login page
    When user enters user id/password cred
    And User click the login icon
    Then user successfully logged in home page

    @first_check
    Scenario: Validation for parameter report
      When Navigate to report and click on parameter icon
      Then enter client details and click on search
      Then Report should generate successfully
    @second_check
    Scenario: Validation for Device dashboard
      When User navigates to health/Alert Dashboard
      And select the client/model name and device ip
      Then User should able to see the report status
    @Third_check
    Scenario: Validation for session count
      When User navigates to Home-->Monitoring dashboard
      Then User should able to see the report status1
    @Forth_check
    Scenario: Validation for Topology
      When User Navigates to HOME-->Configuration-->User Session
      And enter the IP address and select the session ip
      Then User should able to see the status report2
    @fifth_check
    Scenario: Validation for health diagnosis
      When user Navigates to home-->Diagnosis dashboard
      And User should able to see the report status3







