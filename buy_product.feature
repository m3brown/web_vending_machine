Feature: Buy Product
  As a vending machine customer,
  I want to buy products
  So that I can enjoy a tasty treat

Background: I am at the vending machine

Scenario: Buy a product from the vending machine
  Given I have inserted a quarter
  When I purchase a product
  Then I should receive the product
