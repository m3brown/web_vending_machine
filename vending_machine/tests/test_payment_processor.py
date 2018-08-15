from vending_machine.payments import PaymentProcessor
from django.test import TestCase
from vending_machine.sql_command import SQLCommand

sql = SQLCommand()

class TestPaymentProcessor():
    def setUp(self):
        self.processor = PaymentProcessor()

    def tearDown(self):
        sql.execute('DELETE from vending_machine_payment')

    def test_is_payment_made_with_no_payment(self):
        # Arrange

        # Act
        result = self.processor.is_payment_made()

        # Assert
        assert result == False

    def test_is_payment_made_with_a_payment(self):
        # Arrange
        self.processor.make_payment(1)

        # Act
        result = self.processor.is_payment_made()

        # Assert
        assert result == True

    def test_make_payment_expects_payment_nonzero(self):
        # Arrange

        # Act
        self.processor.make_payment(1)

        # Assert
        assert self.processor.get_payment_amount() != 0

    def test_process_payment_sets_payment_amount_to_zero(self):
        # Arrange
        self.processor.make_payment(1)

        # Act
        result = self.processor.process_payment()

        # Assert
        assert self.processor.get_payment_amount() == 0
