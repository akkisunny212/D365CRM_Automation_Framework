@smoke
Feature: Services Smoke
  Scenario: Quick service request submission (smoke)
    Given I am logged in
    When I submit a new service request with name "Smoke Service"
    Then the request should be submitted successfully
