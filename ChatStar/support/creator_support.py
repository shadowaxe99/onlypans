```python
import os
from ChatStar.chatbot import chatbot_training
from ChatStar.support import marketing_assistance, community_access

class CreatorSupport:
    def __init__(self, user_data_schema, support_schema):
        self.user_data_schema = user_data_schema
        self.support_schema = support_schema

    def provide_chatbot_training(self, creator_id):
        creator_data = self.user_data_schema.get_creator_data(creator_id)
        chatbot_training.train_chatbot(creator_data['chatbot'])

    def provide_marketing_assistance(self, creator_id):
        creator_data = self.user_data_schema.get_creator_data(creator_id)
        marketing_assistance.assist_marketing(creator_data)

    def provide_community_access(self, creator_id):
        creator_data = self.user_data_schema.get_creator_data(creator_id)
        community_access.grant_access(creator_data)

    def handle_support_request(self, request):
        if request['type'] == 'chatbot_training':
            self.provide_chatbot_training(request['creator_id'])
        elif request['type'] == 'marketing_assistance':
            self.provide_marketing_assistance(request['creator_id'])
        elif request['type'] == 'community_access':
            self.provide_community_access(request['creator_id'])
        else:
            raise ValueError("Invalid support request type")

    def process_support_requests(self):
        pending_requests = self.support_schema.get_pending_requests()
        for request in pending_requests:
            self.handle_support_request(request)
            self.support_schema.mark_request_processed(request['id'])
```