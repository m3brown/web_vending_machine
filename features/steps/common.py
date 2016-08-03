from behave import *
from django.core.urlresolvers import reverse
from nose.tools import *
import time

# @given("I have inserted a quarter")
# def insert_quarter(context):
#     context.test.client.get(reverse('insert_coin'))

# @when("I purchase a product")
# def buy_a_product(context):
#     context.response = context.test.client.get(reverse('buy_product'))

# @then("I should receive the product")
# def assert_recieve_product(context):
#     assert_is_not_none(context.response.json()['product'])

@given("I have inserted a quarter")
def insert_quarter(context):
    insert_button = context.driver.find_element_by_id('insert-btn')
    insert_button.click()

    # time.sleep(0.5)
    # insert_button.click()
    # time.sleep(0.5)
    # insert_button.click()

@when("I purchase a product")
def buy_a_product(context):
    buy_button = context.driver.find_element_by_id('buy-btn')
    buy_button.click()

@then("I should receive the product")
def assert_recieve_product(context):
    message_element = context.driver.find_element_by_id('msg')
    assert_equals(message_element.text, 'Enjoy!')

