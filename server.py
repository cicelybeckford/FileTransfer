import socket
from threading import Thread
import os
import cipher
from SocketServer import ThreadingMixIn

TCP_IP = 'localhost'
TCP_PORT = 7777
BUFFER_SIZE = 1024


class ClientThread(Thread):

    def __init__(self, addr, sock, filename):
        Thread.__init__(self)
        self.addr = addr
        self.sock = sock
        self.filename = filename
        print " New thread started for " + str(addr)

    def run(self):
        exists = os.path.isfile(self.filename)
        if exists:
            data = open(self.filename, 'rb')
            while True:
                line = data.read(BUFFER_SIZE)
                while (line):
                    msg = cipher.encrypt_message(line)
                    self.sock.send(msg)
                    line = data.read(BUFFER_SIZE)
                if not line:
                    data.close()
                    self.sock.close()
                    break
        else:
            msg = cipher.encrypt_message("-1")
            self.sock.send(msg)
            self.sock.close()


tcpsock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(5)
    print "Waiting for incoming connections..."
    conn, addr = tcpsock.accept()
    print 'Got connection from ', addr
    encrypted_filename = conn.recv(BUFFER_SIZE)
    filename = cipher.decrypt_message(encrypted_filename)
    newthread = ClientThread(addr, conn, filename)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()