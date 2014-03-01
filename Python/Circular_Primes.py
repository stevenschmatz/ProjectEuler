import random
import numpy as np

def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

def is_prime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

def is_circular(p):
    digits = map(int, list(str(p)))
    for i in range(len(digits)-1):
        digits = [digits[len(digits)- 1]] + digits[:len(digits)-1]
        if not is_prime(int(''.join(map(str, digits)))):
            return False
    return True

count = 0
for prime in primesfrom2to(1000000):
    if is_circular(prime): 
        count += 1
print count