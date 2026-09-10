Feature: Dropdown
  Scenario: Select Option from Dropdown
    Given I navigate to the dropdown page
    When I select option "2" from the dropdown
    Then the option "2" should be selected
