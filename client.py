import socket
import time
import cipher
import os
from Crypto.Cipher import AES
import base64

TCP_IP = 'fd7a:cef:2cae:0:5f21:91d6:523b:d372'
TCP_PORT = 7777
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

filename = "mytext.txt"


encrypted_filename = cipher.encrypt(filename)
start = time.time()
s.send('%s' % filename)


with open('received_file', 'wb') as f:
    while True:
        #print('receiving data...')
        encrypted_data = s.recv(BUFFER_SIZE)
        data = cipher.decrypt(encrypted_data)
        if data == '-1':
            output = 'Error: File not found'
            finish = time.time()
            break
        else:
            if not data:
                f.close()
                finish = time.time()
                print 'file closed'
                break
            print 'file opened'
            print('data=%s' % data)
            output = 'Successfully got the file'
            # write data to a file
            f.write(data)

print(output)
print("RTT: %s seconds" % str(finish - start))
s.close()
print('connection closed')