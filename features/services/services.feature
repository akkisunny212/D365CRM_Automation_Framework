Feature: Services Module
  Scenario: Submit a new service request
    Given I am logged in
    When I submit a new service request
    Then the request should be submitted successfully
