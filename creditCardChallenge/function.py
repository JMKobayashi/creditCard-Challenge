from cryptography.fernet import Fernet

class creditCardFunction:
    
    def encrypt(value):
        key = open("encrypt.key",'rb').read()
        encoded_value = value.encode()
        fernet = Fernet(key)
        encrypted_value = fernet.encrypt(encoded_value) 

        return encrypted_value
