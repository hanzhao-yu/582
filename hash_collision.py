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
    k = k//16 + 1
    while 1:
        hashedX = sha256(x).hexdigest()
        hashedY = sha256(y).hexdigest()
        if hashedY[64-k:64] == hashedX[64-k:64]:
            break
        x = ''.join(random.choice(letters) for i in range(10)).encode('utf-8')
        y = ''.join(random.choice(letters) for i in range(10)).encode('utf-8')
    
    return( x, y )