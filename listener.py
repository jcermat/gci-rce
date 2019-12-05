import os
import socket
import shlex

rhost="10.10.10"
rport=9002

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("10.10.16.3", 9002))
sock.listen(1)
print("listening...")
con, addr = sock.accept()
print("connected to " + rhost)
while True:
    cmd = input("> ")
    con.sendall(cmd.encode("utf-8"))
    print(con.recv(4096).decode("utf-8"))
sock.close()
