```python
import json
from ..user_data import UserData
from ..payment import Payment

class PremiumContent:
    def __init__(self):
        self.user_data = UserData()
        self.payment = Payment()

    def get_premium_content(self, user_id):
        user = self.user_data.get_user(user_id)
        if not user:
            return "User not found"

        premium_content = user.get('premium_content')
        if not premium_content:
            return "No premium content available"

        return premium_content

    def purchase_premium_content(self, user_id, content_id):
        user = self.user_data.get_user(user_id)
        if not user:
            return "User not found"

        premium_content = self.get_premium_content(user_id)
        content_to_purchase = [content for content in premium_content if content['id'] == content_id]

        if not content_to_purchase:
            return "Content not found"

        content_price = content_to_purchase[0]['price']
        payment_status = self.payment.process_payment(user_id, content_price)

        if payment_status == "Payment successful":
            user['purchased_content'].append(content_to_purchase[0])
            self.user_data.update_user(user_id, user)
            return "Content purchased successfully"

        return "Payment failed"
```