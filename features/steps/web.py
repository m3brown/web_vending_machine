from behave import *
from selenium import webdriver
import time

@given("I am at the vending machine")
def arrive_at_vending_machine(context):
    context.driver = webdriver.Chrome('./vendor/chromedriver')
    context.driver.get('localhost:8000')

@given("I have inserted a quarter")
def insert_quarter(context):
    insert_button = context.driver.find_element_by_id('insert-btn')
    insert_button.click()

@when("I purchase a product")
def buy_a_product(context):
    buy_button = context.driver.find_element_by_id('buy-btn')
    buy_button.click()

@then("I should receive the product")
def assert_recieve_product(context):
    message_element = context.driver.find_element_by_id('msg')
    assert message_element.text == 'Enjoy!'

@then("I should receive nothing")
def assert_recieve_product(context):
    message_element = context.driver.find_element_by_id('msg')
    assert message_element.text == 'Please insert money'
