from django.test import TestCase
from django.core.urlresolvers import reverse
from vending_machine.vending_machine import VendingMachine
from nose.tools import *

# Create your tests here.
class IndexTests(TestCase):
    def test_index_page_expects_success(self):
        # Arrange

        # Act
        response = self.client.get(reverse('index'))

        # Assert
        assert_equals(response.status_code, 200)
        assert_equals(response.context['msg'], 'Please insert money')

class InsertCoinTests(TestCase):
    def setUp(self):
        VendingMachine().reset()

    def test_insert_coin_expects_success_msg(self):
        # Arrange

        # Act
        response = self.client.get(reverse('insert_coin'))

        # Assert
        assert_equals(response.status_code, 200)
        assert_equals(response.json()['msg'], 'You have inserted $0.25')

class BuyProductTests(TestCase):
    def setUp(self):
        VendingMachine().reset()

    def test_buy_product_without_payment_expects_error_msg(self):
        # Arrange

        # Act
        response = self.client.get(reverse('buy_product'))

        # Assert
        assert_equals(response.status_code, 200)
        assert_equals(response.json()['msg'], 'Cannot buy product without payment')

    def test_buy_product_with_payment_expects_success_msg(self):
        # Arrange
        self.client.get(reverse('insert_coin'))

        # Act
        response = self.client.get(reverse('buy_product'))

        # Assert
        assert_equals(response.status_code, 200)
        assert_equals(response.json()['msg'], 'Enjoy!')

