import socket
import _thread
from time import sleep

# Create a socket and bind it to the port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 1984))
s.listen(5)
print("Listening for connections...")
allowed_ip=["150","100","110"]

# Function to handle communication with a single client
def handle_client(conn):
    while True:
        data = conn.recv(1024)  # Receive data from the client
        if not data:
            break
        print('Received:', data.decode())  # Decode and print the message
        acknowledgement = f"Server acknowledged: {data.decode()}"
        conn.sendall(acknowledgement.encode())  # Send acknowledgment to the client
    conn.close()
    print("closing connection")# Close the connection when done

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

