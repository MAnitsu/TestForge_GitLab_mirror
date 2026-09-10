Feature: Dynamic Loading
  Scenario: Load Hidden Element
    Given I navigate to the dynamic loading page
    When I click the start button
    And I wait for the loading to complete
    Then I should see the final message
