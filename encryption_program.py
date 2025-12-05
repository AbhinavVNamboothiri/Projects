import string
import random

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = chars.copy()

# Shuffling the key
random.shuffle(key)

# Encryption 

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for i in plain_text:
    index = chars.index(i)
    cipher_text += key[index]

print(f"Plain text: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# Decryption

cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for i in cipher_text:
    index = key.index(i)
    plain_text += chars[index]

print(f"Cipher text: {cipher_text}")
print(f"Decrypted message: {plain_text}")

