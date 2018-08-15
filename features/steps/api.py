from behave import *
from django.core.urlresolvers import reverse
import time
from vending_machine.vending_machine import VendingMachine

#@given("I am at the vending machine")
#def arrive_at_vending_machine(context):
#    context.vending_machine = VendingMachine()
#    time.sleep(2)
#
#@given("I have inserted a quarter")
#def insert_quarter(context):
#    context.vending_machine.insert_coin(1)
#
#@when("I purchase a product")
#def buy_a_product(context):
#    context.product = context.vending_machine.buy_product()
#
#@then("I should receive the product")
#def assert_recieve_product(context):
#    assert context.product == 'product'
#
#@then("I should receive nothing")
#def assert_recieve_product(context):
#    assert context.product == None
