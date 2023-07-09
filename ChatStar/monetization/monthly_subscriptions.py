```python
import datetime
from ..user_data import UserData
from ..payment_schema import PaymentSchema

class MonthlySubscription:
    def __init__(self, user_data: UserData, payment_schema: PaymentSchema):
        self.user_data = user_data
        self.payment_schema = payment_schema

    def process_subscription(self, user_id: str, subscription_price: float):
        user = self.user_data.get_user(user_id)
        if not user:
            return "User not found"

        payment_details = self.payment_schema.get_payment_details(user_id)
        if not payment_details:
            return "Payment details not found"

        if self.payment_schema.process_payment(payment_details, subscription_price):
            self.user_data.update_subscription_status(user_id, True)
            self.user_data.update_subscription_date(user_id, datetime.datetime.now())
            return "Subscription successful"
        else:
            return "Payment failed"

    def check_subscription_status(self, user_id: str):
        user = self.user_data.get_user(user_id)
        if not user:
            return "User not found"

        if user['subscription_status']:
            return "User is subscribed"
        else:
            return "User is not subscribed"
```