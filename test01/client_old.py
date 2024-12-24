import socket
import _thread

def receive_messages(sock):
    while True:
        data = sock.recv(1024)  # Receive data from the server
        if not data:
            break
        print(f"Server: {data.decode()}")  # Print the acknowledgment or server message

def send_messages(sock):
    while True:
        message = input("Enter message: ")
        sock.sendall(message.encode())
    

def start_client(server_ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, port))

    _thread.start_new_thread(receive_messages, (s,))
    _thread.start_new_thread(send_messages, (s,))

    while True:
        # This loop keeps the main thread alive
        pass

server_ip = '192.168.208.238'  # Replace with the server's IP address
port = 1984
start_client(server_ip, port)
