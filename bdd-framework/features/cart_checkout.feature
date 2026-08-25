Feature: Cart
  As a shopper
  I want to add products to my cart
  So that I can proceed to checkout

  Scenario: Add a product to the cart
    Given I am on the home page
    When I add "Blue Top" to the cart
    And I go to my cart
    Then "Blue Top" should be in my cart
