import math

def num_BTC(b):
    res = b % 210000
    order = b // 210000
    c = float(21000000 - (21000000 - 50 * res) * (0.5 ** order))
    return c
