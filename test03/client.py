import socket
import _thread
import network
from time import sleep

def change_ip(end):
    wifi = network.WLAN(network.STA_IF)
    original_ip = wifi.ifconfig()[0]
    ip_parts = original_ip.split('.')
    ip_parts[-1] = str(end)  # Set your desired last part here
    static_ip = '.'.join(ip_parts)
    # Get subnet mask, gateway, and DNS from the current configuration
    subnet_mask, gateway, dns = wifi.ifconfig()[1], wifi.ifconfig()[2], wifi.ifconfig()[3]
    # Set the new static IP configuration
    wifi.ifconfig((static_ip, subnet_mask, gateway, dns))
    print("IP address:", wifi.ifconfig()[0])

def receive_messages(sock):
    while True:
        data = sock.recv(1024)
        print(data.decode())  # Print the acknowledgment or server message

def send_messages(sock,message):
    sock.sendall(message.encode())  

def start_client(server_ip, port):
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, port))
    _thread.start_new_thread(receive_messages, (s,))

server_ip = '192.168.204.238'  # Replace with the server's IP address
port = 1984
change_ip(200)
start_client(server_ip,port)
send_messages(s,"1")
sleep(.5)
send_messages(s,"2")
sleep(0.5)






