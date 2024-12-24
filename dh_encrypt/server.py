import socket
import _thread
from time import sleep
from dh_utils import *
from cryptoPrimitives import crypt

allowed_ip=["150","100","110"]
port=1984


def setup_client(conn):
    data=conn.recv(1024)
#     internal_encryption = crypt(network_key)
#     data=internal_encryption.decrypt(data)
    client_public_key=int(data)
    conn.sendall(str(public_key).encode())
    shared_key= generate_shared_key(client_public_key, private_key)
    print("Shared Key obtained",shared_key)
    return shared_key

# Function to handle communication with a single client
def handle_client(conn):
    shared_key=setup_client(conn)
    shared_key=str(shared_key).encode()
    if len(shared_key) < 32:
        aes_key = shared_key + b'\x00' * (32 - len(shared_key))  # Pad with null bytes
    else:
        aes_key = shared_key[:32]
    c = crypt(aes_key)
    while True:
        data = conn.recv(1024)# Receive data from the client
        if not data:
            break
        data=c.decrypt(data)
        print('Received:', data)  # Decode and print the message
        acknowledgement = f"Server acknowledged: {data}"
        conn.sendall(acknowledgement.encode())  # Send acknowledgment to the client
    conn.close()
    
    
def setup_server_node(allowed_ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen(5)
    print("Listening for connections...")
    global private_key
    private_key = generate_private_key()
    global public_key
    public_key = generate_public_key(private_key)
    # Main loop to accept new client connections
    while True:
        conn, addr = s.accept()  # Accept a new connection
        print('Connection request with', addr[0])
        if addr[0].split(".")[-1] not in allowed_ip:
            conn.close()
            print('Connection request with', addr[0],"rejected")
        else:
            print('Connection request with', addr[0],"accepted")
            _thread.start_new_thread(handle_client, (conn,))  # Start a new thread for the client

setup_server_node(allowed_ip,port)









