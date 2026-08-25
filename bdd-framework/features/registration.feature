Feature: User Registration
  As a new visitor
  I want to register an account
  So that I can shop on the site

  Scenario: Successful registration with valid details
    Given I am on the login page
    When I sign up with a new unique email
    And I complete the account information form
    Then my account should be created

  Scenario: Registration fails with an email that is already registered
    Given I am on the login page
    When I start signup with name "Existing User" and email "valid.user@example.com"
    Then I should see an email already exists error

  Scenario Outline: Registration succeeds regardless of account title
    Given I am on the login page
    When I sign up with a new unique email
    And I complete the account information form with title "<title>"
    Then my account should be created

    Examples:
      | title |
      | Mr    |
      | Mrs   |
