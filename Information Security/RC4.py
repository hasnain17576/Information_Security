def arc4crypt(data, key):
    x = 0
    box = list(range(256))  
    for i in range(256):
        x = (x + box[i] + ord(key[i % len(key)])) % 256
        box[i], box[x] = box[x], box[i]  
    x = 0
    y = 0
    out = []
    for char in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]  
        out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))  
    return "".join(out)
key = 'SuperSecretKey!!'
origtext = 'Dive Dive Dive'
ciphertext = arc4crypt(origtext, key)
plaintext = arc4crypt(ciphertext, key)
print('The original text is: {}'.format(origtext))
print('The ciphertext is: {}'.format(ciphertext))
print('The plaintext is: {}'.format(plaintext))