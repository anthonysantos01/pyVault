# crypto.py
import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.fernet import Fernet
import base64
STATIC_KEY = b'6hVJzYYyGzN0Pn60wM23jV0kIqDoQoWx2pT5CpziJWs='  
cipher_suite = Fernet(STATIC_KEY)

AES_KEY = b"XBBlHl65KphO6rHC"  
AES_IV = os.urandom(16)  

def get_aes_key():
    return AES_KEY


def encrypt_file(file_path):
    if not os.path.exists("passwords.vlt"):
        with open("passwords.vlt", "w") as tmpfile:
            pass
    key = get_aes_key()
    cipher = Cipher(algorithms.AES(key), modes.CBC(AES_IV))
    padder = padding.PKCS7(128).padder()

    with open(file_path, 'rb') as file:
        file_data = file.read()
        padded_data = padder.update(file_data) + padder.finalize()

    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    encrypted_file_path = file_path
    with open(encrypted_file_path, 'wb') as enc_file:
        enc_file.write(AES_IV + encrypted_data)

def decrypt_file(file_path):
    key = get_aes_key()

    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    iv = encrypted_data[:16] 
    encrypted_data = encrypted_data[16:] 

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(padded_data) + unpadder.finalize()

    decrypted_file_path = file_path.replace(".enc", ".dec")
    with open(decrypted_file_path, 'wb') as dec_file:
        dec_file.write(decrypted_data)


def encrypt_password(password):
   
    return cipher_suite.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    
    return cipher_suite.decrypt(encrypted_password.encode()).decode()