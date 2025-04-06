Feature: Coach views all member invoices

  Scenario: View all invoices
    Given I am logged in as a Coach
    When I go to the invoices page
    Then I should see invoices for all members