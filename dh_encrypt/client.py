#client code

import socket
import _thread
import network
from time import sleep
from dh_utils import *
from cryptoPrimitives import crypt


def change_ip(end):
    wifi = network.WLAN(network.STA_IF)
    original_ip = wifi.ifconfig()[0]
    ip_parts = original_ip.split('.')
    ip_parts[-1] = str(end) 																 # Set your desired last part here
    static_ip = '.'.join(ip_parts)
    subnet_mask, gateway, dns = wifi.ifconfig()[1], wifi.ifconfig()[2], wifi.ifconfig()[3]	# Get subnet mask, gateway, and DNS from the current configuration
    wifi.ifconfig((static_ip, subnet_mask, gateway, dns))									# Set the new static IP configuration
    print("IP address:", wifi.ifconfig()[0])

def receive_messages(sock):
    while True:
        data = sock.recv(1024)
        print(data.decode())
            
def send_messages(sock,message):
    encrypted_message = c.encrypt(message)  # Encode plain text to bytes
    sock.sendall(encrypted_message)  

def start_client(server_ip, port):
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, port))
    
def setup_client_node(server_ip, port,ip_end):
    change_ip(ip_end)
    start_client(server_ip,port)
    private_key = generate_private_key()
    public_key = generate_public_key(private_key)
    internal_encryption = crypt(network_key)
#     print(internal_encryption.encrypt(str(public_key)))
    s.sendall(internal_encryption.encrypt(str(public_key)))
#     s.sendall(str(public_key).encode())
    data = s.recv(1024)
    data=internal_encryption.decrypt(data)
    server_public_key=int(data)
    shared_key=generate_shared_key(server_public_key, private_key)
    print("Shared key:",shared_key)
    shared_key=str(shared_key).encode()
    if len(shared_key) < 32:
        aes_key = shared_key + b'\x00' * (32 - len(shared_key))  # Pad with null bytes
    else:
        aes_key = shared_key[:32]
    global c
    c = crypt(aes_key)
    _thread.start_new_thread(receive_messages, (s,))
    
server_ip = '192.168.185.238'
port = 1984

setup_client_node(server_ip, port,ip_end="150")

send_messages(s,"hi")
sleep(.5)














