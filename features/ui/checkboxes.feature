Feature: Checkboxes
  Scenario: Check and Uncheck Boxes
    Given I navigate to the checkboxes page
    When I check checkbox 0
    And I uncheck checkbox 1
    Then checkbox 0 should be checked
    And checkbox 1 should be unchecked
