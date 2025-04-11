Feature: Member views their invoices

  Scenario: View invoice summary
    Given I am logged in as Member user_id 4
    When I go to My Invoices
    Then I should see invoices where user_id = 4

  Scenario: View invoice details
    Given I open invoice id 2
    Then I should see all items related to invoice 2
