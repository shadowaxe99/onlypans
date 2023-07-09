```python
import os
from cryptography.fernet import Fernet

class Privacy:
    def __init__(self, user_data_schema):
        self.user_data_schema = user_data_schema
        self.key = os.environ.get('ENCRYPTION_KEY')
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, data):
        encoded_data = data.encode()
        encrypted_data = self.cipher_suite.encrypt(encoded_data)
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        return decrypted_data.decode()

    def anonymize_data(self):
        anonymized_data = {}
        for key, value in self.user_data_schema.items():
            if key not in ['username', 'email']:
                anonymized_data[key] = self.encrypt_data(value)
        return anonymized_data

    def de_anonymize_data(self, anonymized_data):
        de_anonymized_data = {}
        for key, value in anonymized_data.items():
            if key not in ['username', 'email']:
                de_anonymized_data[key] = self.decrypt_data(value)
        return de_anonymized_data
```