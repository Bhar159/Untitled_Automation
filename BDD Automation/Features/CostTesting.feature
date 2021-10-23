Feature: Functionality to check (Cost utilization)

  Scenario Outline: validate the cost ultilization
    Given User open the login page
    When User enter the username "<Username>" and password "<Password>"
    Then User should be able to login successfully
    When User click on Configuration Icon
    Then User able to see the cost utilization report

    Examples: User cred
      | Usernamr  | Password  |
      | vikkrams  | pass@123  |
      | User      | Psw       |

