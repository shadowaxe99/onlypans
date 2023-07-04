```python
import json
from chatbot_training import train_chatbot

class Chatbot:
    def __init__(self, creator_id, chatbot_schema):
        self.creator_id = creator_id
        self.chatbot_schema = chatbot_schema
        self.chatbot_model = None

    def load_chatbot(self):
        try:
            with open(f'{self.creator_id}_chatbot.json', 'r') as file:
                self.chatbot_model = json.load(file)
        except FileNotFoundError:
            print("Chatbot model not found. Training new model.")
            self.train_chatbot()

    def save_chatbot(self):
        with open(f'{self.creator_id}_chatbot.json', 'w') as file:
            json.dump(self.chatbot_model, file)

    def train_chatbot(self):
        self.chatbot_model = train_chatbot(self.chatbot_schema)
        self.save_chatbot()

    def respond_to_message(self, message):
        # This is a placeholder for the actual chatbot response logic
        # which would be based on the trained chatbot model
        response = "Hello, I'm your chatbot!"
        return response
```