import urandom
# Define the prime number p and generator g (for example purposes, use a larger safe prime)
p = 0xFFFFFFFB  # Example of a large safe prime
# network_key=0xFFFFFFFB
network_key=b'1118084954\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
g = 2  # Common choice of generator

def bit_length(n):
    return len(bin(n)) - 2

# Function to generate a public key: A = g^a % p
def generate_public_key(private_key):
    return pow(g, private_key, p)

# Function to generate a shared key: Shared Key = B^a % p (for Alice)
def generate_shared_key(other_public_key, private_key):
    return pow(other_public_key, private_key, p)

# Function to generate a random private key in the range of 1 to p-2
def generate_private_key():
    return urandom.getrandbits(32) % (p - 2) + 1

def exhange_keys():
    pass
    



