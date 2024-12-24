import socket
import _thread
from time import sleep

# Custom queue implementation for MicroPython
class SimpleQueue:
    def __init__(self):
        self.queue = []
        self.lock = _thread.allocate_lock()

    def put(self, item):
        with self.lock:
            self.queue.append(item)

    def get(self):
        with self.lock:
            if len(self.queue) > 0:
                return self.queue.pop(0)
            return None

    def is_empty(self):
        with self.lock:
            return len(self.queue) == 0

# Create a thread-safe queue
message_queue = SimpleQueue()

def receive_messages(sock):
    while True:
        data = sock.recv(1024)
        print(data.decode())


def send_messages(sock):
    while True:
        try:
            if not message_queue.is_empty():
                message = message_queue.get()
                sock.sendall(message.encode())
        except Exception as e:
            print("Error sending message:", e)
            break

def start_client(server_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server_ip, port))
        print("Connected to server:", server_ip, port)
        
        # Start threads for sending and receiving
        _thread.start_new_thread(receive_messages, (s,))
        _thread.start_new_thread(send_messages, (s,))
        
    except Exception as e:
        print("Error in client:", e)

# Replace with your server's IP address
server_ip = '192.168.208.238'
port = 1984

start_client(server_ip, port)

# Enqueue messages for sending
message_queue.put("1")
sleep(1)  # Simulate delay
message_queue.put("2")
sleep(1)
