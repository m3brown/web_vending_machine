import unittest
from nose.tools import *
from vending_machine.payments import PaymentProcessor
from vending_machine.models import Payment
from django.test import TestCase

class TestPaymentProcessor(TestCase):
    def setUp(self):
        self.processor = PaymentProcessor()
        Payment.objects.update_or_create(pk=1, defaults={'amount':0})

    def test_is_payment_made_with_no_payment(self):
        # Arrange

        # Act
        result = self.processor.is_payment_made()

        # Assert
        assert_false(result)

    def test_is_payment_made_with_a_payment(self):
        # Arrange
        self.processor.make_payment(1)

        # Act
        result = self.processor.is_payment_made()

        # Assert
        assert_true(result)

    def test_make_payment_expects_payment_nonzero(self):
        # Arrange

        # Act
        self.processor.make_payment(1)

        # Assert
        assert_not_equal(0, self.processor.payment_amount())

    def test_reset_sets_payment_amount_to_zero(self):
        # Arrange
        self.processor.make_payment(1)

        # Act
        self.processor.reset()

        # Assert
        assert_equal(0, self.processor.payment_amount())
