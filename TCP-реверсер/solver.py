import socket
import time
import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('tcp.innoctf.hackforces.com',5090))
while True:
#if True==True:
    data = s.recv(1024).decode('utf-8')
    data = data.replace('\r', '').replace('\n','').replace('Good job!', '').replace('progress!','')
    print(data)
    
    print(data[::-1])
    #e = input(':')
    s.send(bytes(data[::-1]+"\n", 'UTF-8'))
    
    time.sleep(0.25)
s.close()