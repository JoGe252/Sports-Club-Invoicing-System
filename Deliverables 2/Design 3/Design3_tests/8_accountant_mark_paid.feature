Feature: Accountant marks invoice as paid

  Scenario: Mark unpaid invoice as paid
    Given I am logged in as Accountant
    And invoice id 5 is unpaid
    When I click "Mark as Paid"
    Then the paid field of invoice 5 should be true
