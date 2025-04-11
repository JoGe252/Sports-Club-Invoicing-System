Feature: Admin creates invoices

  Scenario: Admin creates invoice for member
    Given I am logged in as Admin
    When I open the Create Invoice form
    And I select member user_id 2
    And I enter issued_date "2025-04-10" and due_date "2025-04-25"
    Then the invoice should be saved with user_id = 2