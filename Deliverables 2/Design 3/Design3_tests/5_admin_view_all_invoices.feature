Feature: Admin views all invoices

  Scenario: View invoice list
    Given I am logged in as Admin
    When I open the Invoices page
    Then I should see a list of all invoices in the system
