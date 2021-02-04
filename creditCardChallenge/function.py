from cryptography.fernet import Fernet

class creditCardFunction:
    
    def encrypt(value):
        key = b'8lH6QQcT1uQ-7fM0JOg1qZWtSuKbxWOO11i3ytXKDjA='
        encoded_value = value.encode()
        fernet = Fernet(key)
        encrypted_value = fernet.encrypt(encoded_value) 

        return encrypted_value

    def decrypt(value):
        key = b'8lH6QQcT1uQ-7fM0JOg1qZWtSuKbxWOO11i3ytXKDjA='
        fernet = Fernet(key)
        decrypted_value = fernet.decrypt(value)

        decrypted_value.decode('utf-8')

        return decrypted_value
