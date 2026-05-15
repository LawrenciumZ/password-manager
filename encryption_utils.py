import os 
from cryptography.fernet import Fernet

def generate_key(path="data/secret.key"):
    key = Fernet.generate_key()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as key_file:
        key_file.write(key)
        
def load_key(path="data/secret.key"):
    return open(path, "rb").read()

def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message.decode()

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message.encode())
    return decrypted_message.decode()