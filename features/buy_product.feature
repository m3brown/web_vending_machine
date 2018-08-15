Feature: Buy Product

  As a vending machine customer,
  I want to buy products
  So that I can enjoy a tasty treat

Scenario: Buy a product from the vending machine

  Given I am at the vending machine
  and I have inserted a quarter
  When I purchase a product
  Then I should receive the product

Scenario: Buy a product from the vending machine without entering money

  Given I am at the vending machine
  When I purchase a product
  Then I should receive nothing
