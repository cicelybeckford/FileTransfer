import socket

TCP_IP = 'fd7a:cef:2cae:0:5b57:5010:9122:3cc5'
TCP_PORT = 7777
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

filename = "mytextt.txt"
s.send(filename)

with open('received_file', 'wb') as f:
    while True:
        #print('receiving data...')
        data = s.recv(BUFFER_SIZE)
        if data == '-1':
            output = 'Error: File not found'
            break
        else:
            if not data:
                f.close()
                print 'file closed'
                break
            print 'file opened'
            print('data= %s' % data)
            output = 'Successfully got the file'
            # write data to a file
            f.write(data)

print(output)
s.close()
print('connection closed')