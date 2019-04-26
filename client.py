import socket
import cipher


TCP_IP = 'localhost'
TCP_PORT = 7777
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

filename = "infile.txt"
ciphertext = cipher.encrypt_message(filename)
s.send(ciphertext)

with open('received_file', 'wb') as f:
    while True:
        encrypted_data = s.recv(BUFFER_SIZE)
        data = cipher.decrypt_message(encrypted_data)
        if data == '-1':
            output = 'Error: File not found'
            break
        else:
            if not data:
                f.close()
                print 'file closed'
                break
            print 'file opened'
            print('data = %s' % data)
            output = 'Successfully got the file'
            f.write(data)

print(output)
s.close()
print('connection closed')