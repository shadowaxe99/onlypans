```python
import stripe
from ..user_data import UserData
from ..payment_schema import PaymentSchema

stripe.api_key = "your_stripe_api_key"

class PayPerMessage:
    def __init__(self):
        self.user_data = UserData()
        self.payment_schema = PaymentSchema()

    def process_payment(self, user_id, message_count):
        user = self.user_data.get_user(user_id)
        price_per_message = self.payment_schema.get_price_per_message(user_id)

        total_amount = price_per_message * message_count

        try:
            charge = stripe.Charge.create(
                amount=total_amount,
                currency="usd",
                customer=user['stripe_customer_id'],
                description=f"Payment for {message_count} messages"
            )
            return charge
        except Exception as e:
            print(f"Payment failed: {str(e)}")
            return None

    def update_user_balance(self, user_id, charge):
        if charge:
            self.user_data.update_balance(user_id, charge['amount'])
            return True
        return False
```