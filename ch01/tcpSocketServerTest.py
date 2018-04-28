# -*- coding: utf-8 -*-

import socket
import threading
import time


def deadClient(sock, addr):
    print "Accept new conn from %s:%s" % addr
    sock.send(b"Hello, I am Server")
    while True:
        data  = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode("utf-8") == "exit":
            break
        print "recv data: %s" % data.decode("utf-8")
        sock.send("Loop_msg: %s" % data.decode("utf-8").encode("utf-8"))
    sock.close()
    print "Connection from %s:%s closed!" % addr

if __name__ == "__main__":
    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 9999))
    s.listen(5)
    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=deadClient, args=(sock, addr))
        t.start()