from payments import PaymentProcessor

class VendingMachine:
    def __init__(self):
        self.payment_processor = PaymentProcessor()
        self.message = ''



    def release_change(self):
        if self.payment_processor.is_payment_made():
            return 1
        else:
            return 0

    def insert_coin(self, count):
        self.payment_processor.make_payment(count)
        amount = float(self.payment_processor.get_payment_amount()) / 100.0
        self.message = "You have inserted $%s" % amount

    def buy_product(self):
        if self.payment_processor.is_payment_made():
            self.message = 'Enjoy!'
            self.payment_processor.process_payment()
            return 'product'
        else:
            self.message = 'Please insert money'
            return None
            #raise RuntimeError("Cannot buy product without payment")

    def get_message(self):
        return self.message

    def reset(self):
        '''
        Clear out any money that was in the machine
        '''
        self.payment_processor = PaymentProcessor()
