
import network

# Replace these with your Wi-Fi credentials
ssid = "TSK"
password = "atlu6996"

# Connect to Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

# Wait for connection
while not wifi.isconnected():
    pass

print("Connected to Wi-Fi")
print("IP address:", wifi.ifconfig()[0])

