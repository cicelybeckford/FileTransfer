import socket

#TCP_IP = 'fdef:7597:b371:0:54a7:2b5d:1747:d3aa'
TCP_IP = 'localhost'
TCP_PORT = 7777
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

filename = "mytexbbcccct.txt"
s.send('%s\n' % filename)

with open('received_file', 'wb') as f:
    while True:
        #print('receiving data...')
        data = s.recv(BUFFER_SIZE)
        if data == '-1':
            output = 'Error: File not found'
            break
        else:
            print 'file opened'
            print('data=%s' % data)
            output = 'Successfully got the file'
            if not data:
                f.close()
                print 'file close()'
                break
            # write data to a file
            f.write(data)

print(output)
s.close()
print('connection closed')