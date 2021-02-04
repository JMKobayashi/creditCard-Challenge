from cryptography.fernet import Fernet

class creditCardFunction:
    
    def encrypt(value):
        key = b'8lH6QQcT1uQ-7fM0JOg1qZWtSuKbxWOO11i3ytXKDjA='
        encoded_value = value.encode()
        fernet = Fernet(key)
        encrypted_value = fernet.encrypt(encoded_value) 

        return encrypted_value.decode("utf-8")

    def decrypt(value):
        key = b'8lH6QQcT1uQ-7fM0JOg1qZWtSuKbxWOO11i3ytXKDjA='
        fernet = Fernet(key)
        encoded_value = bytes(value,'utf-8')
        decryptedMessage = fernet.decrypt(encoded_value)
        decode = decryptedMessage.decode()

        return decode
