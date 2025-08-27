@regression
Feature: Services Regression
  Scenario: Submit a new service request (regression)
    Given I am logged in
    When I submit a new service request with name "Regression Service"
    Then the request should be submitted successfully
