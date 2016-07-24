import unittest
from nose.tools import *
from vending_machine.vending_machine import VendingMachine
from vending_machine.models import Payment

class TestVendingMachine:
    def setUp(self):
        self.vending_machine = VendingMachine()
        self.vending_machine.reset()

    def test_release_change_when_no_payment_expects_0_change(self):
        # Arrange

        # Act
        result = self.vending_machine.release_change()

        # Assert
        assert_equals(0, result)

    def test_release_change_with_payment_expects_change_returned(self):
        # Arrange
        self.vending_machine.insert_coin(1)

        # Act
        result = self.vending_machine.release_change()

        # Assert
        assert_greater(result, 0)

    @unittest.skip("buy_product now returns an exception")
    def test_buy_product_with_no_payment_expects_nothing(self):
        # Arrange

        # Act
        result = self.vending_machine.buy_product()

        # Assert
        assert_is_none(result)

    def test_buy_product_with_payment_expects_product(self):
        # Arrange
        self.vending_machine.insert_coin(1)

        # Act
        result = self.vending_machine.buy_product()

        # Assert
        assert_is_not_none(result)

    @raises(RuntimeError)
    def test_buy_product_with_no_payment_expects_exception(self):
        # Arrange

        # Act
        result = self.vending_machine.buy_product()

        # Assert

    @raises(RuntimeError)
    def test_buy_multiple_products_with_no_additional_payment(self):
        # Arrange

        # Act
        self.vending_machine.insert_coin(1)
        self.vending_machine.buy_product()
        self.vending_machine.buy_product()

        # Assert

