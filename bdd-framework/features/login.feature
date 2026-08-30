Feature: Login
  As a registered user
  I want to log in to Automation Exercise
  So that I can access my account

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I log in with email "pritamstar@123" and password "Pritam@123"
    Then I should be logged in

  Scenario: Login fails with an incorrect password
    Given I am on the login page
    When I log in with email "valid.user@example.com" and password "WrongPass999"
    Then I should see a login error
