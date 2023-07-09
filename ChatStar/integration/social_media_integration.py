```python
import requests
from ChatStar.user_data import User
from ChatStar.security import data_protection

class SocialMediaIntegration:
    def __init__(self, user: User):
        self.user = user

    def post_to_social_media(self, platform: str, message: str):
        if platform.lower() == "twitter":
            self.post_to_twitter(message)
        elif platform.lower() == "facebook":
            self.post_to_facebook(message)
        elif platform.lower() == "instagram":
            self.post_to_instagram(message)
        else:
            print("Unsupported platform")

    def post_to_twitter(self, message: str):
        twitter_api_url = "https://api.twitter.com/1.1/statuses/update.json"
        headers = {"Authorization": f"Bearer {self.user.twitter_auth_token}"}
        data = {"status": message}
        response = requests.post(twitter_api_url, headers=headers, data=data)
        if response.status_code == 200:
            print("Successfully posted to Twitter")
        else:
            print("Failed to post to Twitter")

    def post_to_facebook(self, message: str):
        facebook_api_url = "https://graph.facebook.com/v10.0/me/feed"
        params = {"access_token": self.user.facebook_auth_token, "message": message}
        response = requests.post(facebook_api_url, params=params)
        if response.status_code == 200:
            print("Successfully posted to Facebook")
        else:
            print("Failed to post to Facebook")

    def post_to_instagram(self, message: str):
        instagram_api_url = "https://graph.instagram.com/me/media"
        params = {"access_token": self.user.instagram_auth_token, "caption": message}
        response = requests.post(instagram_api_url, params=params)
        if response.status_code == 200:
            print("Successfully posted to Instagram")
        else:
            print("Failed to post to Instagram")

    def share_chatbot_link(self):
        message = f"Interact with me on ChatStar! {self.user.chatbot_link}"
        self.post_to_social_media(self.user.preferred_social_media_platform, message)
```
