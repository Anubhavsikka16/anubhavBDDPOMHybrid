Feature: Testing broken links on the homepage navigation


  Scenario: Verify all links on the homepage navigation are working
    Given I am on the homepage
    Then I need to check the if the links are working
    And there is no broken link on the page