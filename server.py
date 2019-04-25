import socket
from threading import Thread
import os
from SocketServer import ThreadingMixIn

#TCP_IP = 'fdef:7597:b371:0:56dc:7907:ee4a:7a64'
TCP_IP = 'localhost'
TCP_PORT = 7777
BUFFER_SIZE = 1024

class ClientThread(Thread):

    def __init__(self,addr,sock,filename):
        Thread.__init__(self)
        self.addr = addr
        self.sock = sock
        self.filename = filename
        print " New thread started for " + str(addr)

    def run(self):
        exists = os.path.isfile(self.filename)
        if exists:
            f = open(self.filename,'rb')
            while True:
                l = f.read(BUFFER_SIZE)
                while (l):
                    self.sock.send(l)
                    # print('Sent ',repr(l))
                    l = f.read(BUFFER_SIZE)
                if not l:
                    f.close()
                    self.sock.close()
                    break
        else:
            self.sock.send("-1")
            self.sock.close()


tcpsock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(5)
    print "Waiting for incoming connections..."
    #(conn, (ip,port)) = tcpsock.accept()
    conn, addr = tcpsock.accept()
    print 'Got connection from ', addr
    filename = ""
    while True:
        data = conn.recv(1)
        if data == '\n':
            break
        filename += data
    newthread = ClientThread(addr, conn, filename)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
