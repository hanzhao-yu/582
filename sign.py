from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair
from fastecdsa.ecdsa import sign

from fastecdsa import curve, ecdsa, keys
from hashlib import sha256

import random
from signing_util import modinv

def sign(m):
    #generate public key
    n = 115792089237316195423570985008687907852837564279074904382605163141518161494337
    (pk, point) = gen_keypair(curve.secp256k1)
    public_key = point
    #generate signature
    k = random.SystemRandom().randint(1,n-1)
    x = k * curve.secp256k1.G.x
    r = x % n
    z = sha256(m.encode('utf-8'))
    z = int(z.hexdigest(), 16)
    s = (modinv(k, n) * ((z+r*pk) % n))%n
    u1 = ((z % n) * modinv(s,n))%n
    u2 = ((r % n) * modinv(s,n))%n
    x1 = u1 * curve.secp256k1.G.x + u2 * point.x
    print(x1%n)
    print((u1 * curve.secp256k1.G.x + u2 * pk * curve.secp256k1.G.x)%n)
    print((u1 + u2 * pk) * curve.secp256k1.G.x)
    print((z + r * pk)/s * curve.secp256k1.G.x)
    print(r)
    print(s)
    return( public_key, [r,s] )
