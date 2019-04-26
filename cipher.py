import base64
import os
from Crypto.Cipher import AES

def encrypt(data):
	BLOCK_SIZE = 16
	PADDING = '{'
	pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
	EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
	secret_key = os.urandom(BLOCK_SIZE)
	print 'encryption key: ' + secret_key
	cipher = AES.new(secret_key)
	# encodes you private info!
	encoded_data = EncodeAES(cipher, data)
	print 'Encrypted data:', encoded_data
	return encoded_data

def decrypt(encrypted_data):
	PADDING = '{'
	DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
	#Key is FROM the printout of 'secret' in encryption
	#below is the encryption.
	encryption = encrypted_data
	key = ''
	cipher = AES.new(key)
	data = DecodeAES(cipher, encryption)
	return data