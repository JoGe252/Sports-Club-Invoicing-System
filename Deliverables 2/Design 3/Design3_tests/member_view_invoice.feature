Feature: Member views their invoices

  Scenario: View own invoices
    Given I am logged in as member "user1"
    When I go to "My Invoices"
    Then I should see a list of my invoices

  Scenario: View invoice details
    Given I am on my invoices list
    When I click on invoice #1
    Then I should see all invoice items and the total