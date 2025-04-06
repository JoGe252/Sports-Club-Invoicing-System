Feature: All users log in

  Scenario: Admin logs in
    Given I am on the login page
    When I enter username "admin" and password "password"
    Then I am redirected to the dashboard

  Scenario: Member logs in
    Given I am on the login page
    When I enter username "user1" and password "password"
    Then I am redirected to the dashboard