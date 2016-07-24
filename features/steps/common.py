from behave import *
from django.core.urlresolvers import reverse
from nose.tools import *

@given("I have inserted a quarter")
def insert_quarter(context):
    context.test.client.get(reverse('insert_coin'))

@when("I purchase a product")
def buy_a_product(context):
    context.response = context.test.client.get(reverse('buy_product'))

@then("I should receive the product")
def assert_recieve_product(context):
    assert_is_not_none(context.response.json()['product'])
