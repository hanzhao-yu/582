from elgamal_util import mod_inverse
import random

from params import p
from params import g

def keygen():
    sk = random.SystemRandom().randint(1,p)
    pk = pow(g, sk, p)
    return pk,sk

def encrypt(pk,m):
    r = random.SystemRandom().randint(1,p)
    c1 = pow(g, r, p)
    c2 = (pow(pk, r, p) * (m % p)) % p
    return [c1,c2]

def decrypt(sk,c):
    m = ((c[1] % p) * (pow(mod_inverse(c[0], p), sk, p))) % p
    return m

