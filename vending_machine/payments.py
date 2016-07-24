from models import Payment

class PaymentProcessor:
    def __init__(self):
        Payment.objects.get_or_create(pk=1, defaults={'amount': 0})

    def is_payment_made(self):
        payment = Payment.objects.get(pk=1)
        return payment.amount > 0

    def make_payment(self, count):
        payment = Payment.objects.get(pk=1)
        payment.amount = payment.amount + count*25
        payment.save()

    def reset(self):
        payment = Payment.objects.get(pk=1)
        payment.amount = 0
        payment.save()

    def payment_amount(self):
        return Payment.objects.get(pk=1).amount
