
def encrypt(key,plaintext):
    ciphertext=""
    for element in plaintext:
        ciphertext += chr(ord('A') + ((ord(element) + key - ord('A')) % 26));
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    for element in ciphertext:
        plaintext += chr(ord('A') + ((ord(element) - key - ord('A')) % 26));
    return plaintext


