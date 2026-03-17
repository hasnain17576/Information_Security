from salsa20 import XSalsa20_xor # type: ignore
from os import urandom

# 24 byte nonce
IV = urandom(24)

# 32 byte key
KEY = b"*secret**secret**secret**secret*"

# message
message = b"IT'S A YELLOW SUBMARINE"

# encryption
ciphertext = XSalsa20_xor(message, IV, KEY)
print("Ciphertext:", ciphertext)

# decryption
decrypted = XSalsa20_xor(ciphertext, IV, KEY)
print("Decrypted:", decrypted.decode())