from hashlib import sha256
import random
import hashlib
import os
import string

def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
   
    #Collision finding code goes here
    letters = string.ascii_letters + string.digits + string.punctuation
    x = ''.join(random.choice(letters) for i in range(10)).encode('utf-8')
    y = ''.join(random.choice(letters) for i in range(10)).encode('utf-8')
    while 1:
        hashedX = sha256(x).hexdigest()
        hashedX = bin(int(hashedX, 16))[2:].zfill(256)
        hashedY = sha256(y).hexdigest()
        hashedY = bin(int(hashedY, 16))[2:].zfill(256)
        if hashedY[256-k:256] == hashedX[256-k:256]:
            break
        x = ''.join(random.choice(letters) for i in range(10)).encode('utf-8')
        y = ''.join(random.choice(letters) for i in range(10)).encode('utf-8')
    
    return( x, y )