def VernamEncDec(text, key):
    result = ""
    ptr = 0
    for char in text:
        result += chr(ord(char) ^ ord(key[ptr]))  
        ptr += 1
        if ptr == len(key):   
            ptr = 0
    return result
key = "thisismykey12345"
while True:
    input_text = input("\nEnter Text To Encrypt:\t")

    ciphertext = VernamEncDec(input_text, key)
    print("\nEncrypted Vernam Cipher Text:\t" + ciphertext)
    plaintext = VernamEncDec(ciphertext, key)
    print("\nDecrypted Vernam Cipher Text:\t" + plaintext)