from Crypto.Cipher import AES
import base64, os

BLOCK_SIZE = 16
PADDING = "{"
KEY = 'q|A\xb6dx\xb1\t\x00Z\x08w\xfb\x14\x19\xae'
IV = '\xdf\xc1\xc6\xad+\xf3Q\xc5\xf2\xed\xb7\xf1\x94\x14\x87\xfe'

def encrypt_message(data):
    padded_data = data + (PADDING * ((BLOCK_SIZE - len(data)) % BLOCK_SIZE))
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    ciphertext = cipher.encrypt(padded_data)
    return ciphertext

def decrypt_message(encoded_ciphertext):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    data = cipher.decrypt(encoded_ciphertext)
    original = data.rstrip(PADDING)
    return original