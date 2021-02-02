from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair
from fastecdsa.ecdsa import sign

from fastecdsa import curve, ecdsa, keys
from hashlib import sha256

import random
from signing_util import modinv

def sign(m):
    #generate public key
    n = 11579208923731619542357098500868790785283756427907490438260516314151816149433
    (pk, point) = gen_keypair(curve.secp256k1)
    public_key = point
    #generate signature
    k = random.SystemRandom().randint(1,256)
    x = k * point.x
    r = x % n
    z = sha256(m.encode('utf-8'))
    z = int(z.hexdigest(), 16)
    s = ((modinv(k, n) % n) * ((z+r*pk) % n))%n
    return( public_key, [r,s] )
