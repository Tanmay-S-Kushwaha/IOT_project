import socket
import _thread
from time import sleep

def receive_messages(sock):
    while True:
        data = sock.recv(1024)
        print(data.decode())  # Print the acknowledgment or server message

def send_messages(sock,message):
    sock.sendall(message.encode())  

def start_client(server_ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, port))



server_ip = '192.168.208.238'  # Replace with the server's IP address
port = 1984

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_ip, port))
_thread.start_new_thread(receive_messages, (s,))
send_messages(s,"1")
sleep(.5)
send_messages(s,"2")
sleep(0.5)






