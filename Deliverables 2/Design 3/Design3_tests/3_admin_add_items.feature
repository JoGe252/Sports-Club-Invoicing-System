Feature: Admin adds items to invoice

  Scenario: Add single invoice item
    Given an invoice with id 1 exists
    When I add item "Membership" with quantity 1 and unit_price 100.00
    Then invoice total should be 100.00

  Scenario: Add multiple items
    Given invoice 1 exists
    When I add "Training" x 2 at 50.00 and "Locker" x 1 at 30.00
    Then the total should be 130.00
