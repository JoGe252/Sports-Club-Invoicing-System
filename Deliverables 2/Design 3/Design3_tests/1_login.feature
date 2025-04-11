Feature: User login authentication

  Scenario: Successful login
    Given I am on the login page
    When I enter valid credentials for "admin"
    Then I should be redirected to the dashboard

  Scenario: Failed login
    Given I am on the login page
    When I enter "wronguser" and "wrongpass"
    Then I should see "Invalid login credentials"