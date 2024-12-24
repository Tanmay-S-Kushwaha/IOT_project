
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

# Get the original dynamic IP address
original_ip = wifi.ifconfig()[0]
ip_parts = original_ip.split('.')
ip_parts[-1] = "150"  # Set your desired last part here
static_ip = '.'.join(ip_parts)

# Get subnet mask, gateway, and DNS from the current configuration
subnet_mask, gateway, dns = wifi.ifconfig()[1], wifi.ifconfig()[2], wifi.ifconfig()[3]

# Set the new static IP configuration
wifi.ifconfig((static_ip, subnet_mask, gateway, dns))


print("Connected to Wi-Fi")
print("IP address:", wifi.ifconfig()[0])


