import socket
import threading
import os
import pyttsx3 as p
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

p.speak('enter sender IP address')
sip=input('Sender IP is =>   ')
p.speak('enter sender port')
sport=int(input('Sender Port No =>   '))
p.speak('enter receiver IP address')
rip=input('Receiver IP is =>   ')
p.speak('enter receiver Port')
rport=int(input('Receiver Port No =>   '))
s.bind((sip,int(sport)))
def send():
    while True:
        msg=input().encode()
        s.sendto(msg, (rip, rport))

def receive():
    while True:
        msg=s.recvfrom(1024)
        if msg[0].decode()=='exit' or msg[0].decode()=='bye':
            print('\t\t\t\t\tFrom Linux Server :-  Bye-Bye')
            s.sendto('exit'.encode(), (rip, rport))
            os._exit(1)
        print('\t\t\t\t\tFrom Linux Server :-  '+msg[0].decode())
        

t1=threading.Thread(target=send)
t2=threading.Thread(target=receive)

t1.start()
t2.start()