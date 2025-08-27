@smoke
Feature: Sales Module
  Scenario: Create a new lead
    Given I am logged in
    When I create a new lead
    Then the lead should be saved successfully
