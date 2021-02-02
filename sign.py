from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys
from hashlib import sha256

import random

def sign(m):
    #generate public key
    n = 115792089237316195423570985008687907852837564279074904382605163141518161494337
    (pk, point) = gen_keypair(curve.secp256k1)
    public_key = point
    #generate signature
    k = random.SystemRandom().randint(1,256)
    x = k * point.x
    r = x % n
    z = sha256(m)
    s = (modinv(k, n) * ((z+r*pk) % n))%n
    return( public_key, [r,s] )


