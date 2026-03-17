import random
def generate_keystream(length, seed):
    random.seed(seed)
    return [random.randint(0,255) for i in range(length)]
def encrypt(plaintext, seed):
    plaintext_bytes = plaintext.encode()
    keystream = generate_keystream(len(plaintext_bytes), seed)
    ciphertext = []
    for i in range(len(plaintext_bytes)):
        c = plaintext_bytes[i] ^ keystream[i]
        ciphertext.append(c)
    return ciphertext
def attack_known_plaintext(plaintext, ciphertext):
    plaintext_bytes = plaintext.encode()
    recovered_keystream = []
    for i in range(len(plaintext_bytes)):
        k = plaintext_bytes[i] ^ ciphertext[i]
        recovered_keystream.append(k)
    return recovered_keystream
plaintext = "HASNAIN"
ciphertext = encrypt(plaintext, 10)
keystream = attack_known_plaintext(plaintext, ciphertext)
print("Ciphertext:", ciphertext)
print("Recovered Keystream:", keystream)