Feature: Member downloads invoice PDF

  Scenario: Export invoice
    Given I am viewing invoice id 3
    When I click "Download PDF"
    Then a PDF file should be downloaded with invoice details
