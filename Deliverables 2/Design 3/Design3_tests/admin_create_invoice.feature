Feature: Admin creates and assigns an invoice

  Scenario: Create invoice with items
    Given I am logged in as an Admin
    When I create an invoice for member "user1"
    And I add "Training Session" with quantity 2 and price 30.00
    Then the invoice total should be 60.00
    And the invoice should appear under user1's account

  Scenario: Assign invoice to member
    Given I am on the invoice creation page
    When I select member "user1"
    Then the invoice is linked to that member