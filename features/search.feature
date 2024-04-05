Feature: Search feature

  @implemented
  Scenario: Check if user can search for results
    Given The user has navigate to Home page
    When User enters valid pattern into Search box field
    And User clicks on Search button
    Then Valid page should get displayed