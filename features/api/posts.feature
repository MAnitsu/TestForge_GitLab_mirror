Feature: Posts API

  Scenario: Retrieve a post by id
    Given the API base URL is configured
    When I request post with id 1
    Then the response status should be 200
    And the response should contain post id 1
