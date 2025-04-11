Feature: Admin assigns invoice to member

  Scenario: Assign invoice
    Given an invoice with id 2 exists
    When I assign it to user_id 3
    Then the invoice user_id should be 3
