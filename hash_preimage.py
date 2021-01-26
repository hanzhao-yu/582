import hashlib
import os

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    letters = string.ascii_letters + string.digits + string.punctuation
    k = len(target_string)
    nonce = ''.join(random.choice(letters) for i in range(10)).encode('utf-8')
    while 1:
        hashed = sha256(nonce).hexdigest()
        hashed = bin(int(hashed, 16))[2:].zfill(256)
        if hashed[256-k:256] == target_string:
            break
        nonce = ''.join(random.choice(letters) for i in range(10)).encode('utf-8')

    return( nonce )