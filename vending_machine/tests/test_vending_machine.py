import pytest
from unittest import skip
from vending_machine.vending_machine import VendingMachine
from vending_machine.models import Payment
from django.db import connection

class TestVendingMachine():



    def setUp(self):
        self.vending_machine = VendingMachine()

    def tearDown(self):
        connection.cursor().execute('DELETE from vending_machine_payment')




    def test_release_change_when_no_payment_expects_0_change(self):
        # Arrange

        # Act
        result = self.vending_machine.release_change()

        # Assert
        assert result == 0

    def test_release_change_with_payment_expects_change_returned(self):
        # Arrange
        self.vending_machine.insert_coin(1)

        # Act
        result = self.vending_machine.release_change()

        # Assert
        assert result > 0

    @skip("buy_product now returns an exception")
    def test_buy_product_with_no_payment_expects_nothing(self):
        # Arrange

        # Act
        result = self.vending_machine.buy_product()

        # Assert
        assert result is None

    def test_buy_product_with_payment_expects_product(self):
        # Arrange
        self.vending_machine.insert_coin(1)

        # Act
        result = self.vending_machine.buy_product()

        # Assert
        assert result is not None

    def test_buy_product_with_no_payment_expects_exception(self):
        # Arrange

        # Act
        with pytest.raises(RuntimeError):
            result = self.vending_machine.buy_product()

        # Assert

    def test_buy_multiple_products_with_no_additional_payment(self):
        # Arrange

        # Act
        self.vending_machine.insert_coin(1)
        self.vending_machine.buy_product()
        with pytest.raises(RuntimeError):
            self.vending_machine.buy_product()

        # Assert
