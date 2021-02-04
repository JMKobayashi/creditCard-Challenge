import cryptography.fernet import Fernet

class creditCardFunction:
    
    def __init__(self):
        self.key = "This_is_not_a_secret_key"


    def encrypt(value):
        encoded_value = value.encode()
        fernet = Fernet(self.key)
        encrypted_value = fernet.encrypt(encoded_value) 

        return encrypted_value.decode("utf-8")
