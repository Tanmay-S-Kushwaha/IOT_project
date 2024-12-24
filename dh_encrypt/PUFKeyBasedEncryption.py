from cryptoPrimitives import crypt
from PUFResponseGeneration import puf_response_generation
from pyUtils import *

import random


def PUFBasedKey(seed_value):
    # Generate a random challenge input for the PUF
    lfsr_challenge_in = generate_random_int(seed_value)

    # Generate a 128-bit PUF response for the given challenge input
    puf_response_128 = puf_response_generation(lfsr_challenge_in)
    print(puf_response_128)
    print(type(puf_response_128))

    puf_response_32_bytes = binary_to_bytes(puf_response_128)
    #print(puf_response_32_bytes)
    return puf_response_32_bytes



def PUFKeyBasedEncryption(seed_value):
    puf_response_32_bytes = PUFBasedKey(seed_value)
    print("PUF_response",puf_response_32_bytes)
    print(type(puf_response_32_bytes))
    # Validate the key
    if len(puf_response_32_bytes) != 16:
        raise ValueError("PUF-based key must be 16 bytes long.")

    key = puf_response_32_bytes
    print("Key:",key)
    print(type(key))

    c = crypt(key)

    plain_text = "Hello World"
    print("Plain Message : ",plain_text)

    #to Encrypt Data
    encrypted_text = c.encrypt(plain_text)  # Encode plain text to bytes
    print("Encrypted Message : ",encrypted_text)

    #to Decrypt Data
    decrypted_text = c.decrypt(encrypted_text)
    print("Decrypted Message : ",decrypted_text)