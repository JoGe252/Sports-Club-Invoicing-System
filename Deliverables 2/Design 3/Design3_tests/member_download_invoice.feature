Feature: Member downloads invoice PDF

  Scenario: Download a PDF
    Given I am logged in as member "user1"
    And I am viewing invoice #1
    When I click "Download PDF"
    Then the invoice is downloaded as a PDF file