from cryptography.fernet import Fernet

class creditCardFunction:
    
    def encrypt(value):
        key = "This_is_not_a_secret_key"
        encoded_value = value.encode()
        fernet = Fernet(key)
        encrypted_value = fernet.encrypt(encoded_value) 

        return encrypted_value.decode("utf-8")
