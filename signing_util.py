#The extended GCD algorithm
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

#Calculate a modular inverse
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1 and g != -1:
        #print( "gcd = %d"%g )
        raise Exception('modular inverse does not exist')
    else:
        return x % m

