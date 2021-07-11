import socket
import time

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))
    msg = s.recv(1024)
    if len(msg)==0:
        continue
    print(msg.decode())