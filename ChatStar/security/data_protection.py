```python
import os
from cryptography.fernet import Fernet
from ChatStar.security.privacy import UserPrivacySettings

class DataProtection:
    def __init__(self):
        self.key = os.environ.get('DATA_ENCRYPTION_KEY')
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, data):
        encoded_data = data.encode()
        encrypted_data = self.cipher_suite.encrypt(encoded_data)
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        return decrypted_data.decode()

    def protect_user_data(self, user_data):
        privacy_settings = UserPrivacySettings(user_data)
        if privacy_settings.is_data_protection_enabled():
            encrypted_data = self.encrypt_data(user_data)
            return encrypted_data
        else:
            return user_data

    def retrieve_user_data(self, encrypted_data):
        privacy_settings = UserPrivacySettings(encrypted_data)
        if privacy_settings.is_data_protection_enabled():
            decrypted_data = self.decrypt_data(encrypted_data)
            return decrypted_data
        else:
            return encrypted_data
```