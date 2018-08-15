from models import Payment
from sql_command import SQLCommand

sql_command = SQLCommand()

class PaymentProcessor():

    def __init__(self):
        '''
        Set up a Payment row with pk=1 and value=0
        '''
        sql_command.execute(
            'DELETE FROM vending_machine_payment'
        )
        sql_command.execute(
            'INSERT INTO vending_machine_payment VALUES (1, 0)'
        )


    def get_payment_amount(self):
        return sql_command.execute_with_result("SELECT amount FROM vending_machine_payment WHERE id=1")


    def is_payment_made(self):
        amount = self.get_payment_amount()
        return amount > 0


    def make_payment(self, count):
        amount = self.get_payment_amount() + count*25
        sql_command.execute(
            "UPDATE vending_machine_payment \
             SET amount=" + str(amount) + " WHERE id=1"
        )


    def process_payment(self):
        amount = self.get_payment_amount()
        if amount > 0:
            sql_command.execute(
                "UPDATE vending_machine_payment SET amount=0 WHERE id=1"
            )
        return amount
