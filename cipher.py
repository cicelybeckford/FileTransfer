from Crypto.Cipher import AES
import base64, os

BLOCK_SIZE = 16
PADDING = "{"
KEY = 'q|A\xb6dx\xb1\t\x00Z\x08w\xfb\x14\x19\xae'
IV = '\xdf\xc1\xc6\xad+\xf3Q\xc5\xf2\xed\xb7\xf1\x94\x14\x87\xfe'

#def generate_secret_key_and_iv():
#    secret_key = os.urandom(BLOCK_SIZE)
#    iv = os.urandom(BLOCK_SIZE)
#    return secret_key, iv

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


######### BEGIN HERE #######
##
##
#private_msg = """
#    Tonight i'll be your naughty girl
#    I'm callin all my girls
#    We're gonna turn this party out
#    I know you want my body
#    Tonight i'll be your naughty girl
#    I'm callin all my girls
#    I see you look me up and down
#    And i came to party
#    """
##padding_character = "{"
#
##key, iv = generate_secret_key_and_iv()
#encrypted_msg = encrypt_message(private_msg)
#decrypted_msg = decrypt_message(encrypted_msg)
#
#print "   Secret Key: %s - (%d)" % (KEY, len(KEY))
#print "Encrypted Msg: %s - (%d)" % (encrypted_msg, len(encrypted_msg))
#print "Decrypted Msg: %s - (%d)" % (decrypted_msg, len(decrypted_msg))
