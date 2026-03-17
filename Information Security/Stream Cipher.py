import random
def generate_keystream(length, seed):
    random.seed(seed)
    keystream = []
    for i in range(length):
        keystream.append(random.randint(0,255))
    return keystream
def encrypt(plaintext, seed):
    plaintext_bytes = plaintext.encode()
    keystream = generate_keystream(len(plaintext_bytes), seed)
    ciphertext = []
    for i in range(len(plaintext_bytes)):
        c = plaintext_bytes[i] ^ keystream[i]
        ciphertext.append(c)
    return ciphertext
def decrypt(ciphertext, seed):
    keystream = generate_keystream(len(ciphertext), seed)
    plaintext = []
    for i in range(len(ciphertext)):
        p = ciphertext[i] ^ keystream[i]
        plaintext.append(p)
    return bytes(plaintext).decode()
message = "HASNAIN"
seed = 10
cipher = encrypt(message, seed)
print("Ciphertext:", cipher)
original = decrypt(cipher, seed)
print("Decrypted:", original)