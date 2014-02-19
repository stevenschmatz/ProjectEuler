import numpy as np
import math
import random

def primesfrom2to(n):
# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
  sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
  sieve[0] = False
  for i in xrange(int(n**0.5)/3+1):
      if sieve[i]:
          k=3*i+1|1
          sieve[((k*k)/3)::2*k] = False
          sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
  return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]  

prime_list=primesfrom2to(10**7)

def miller_rabin(m):
  if m == 2:
    return True
  s=1
  k = 2
  t = (m-1)/2
  while t%2 == 0:
      t /= 2
      s += 1

  for r in range(0,k):
      rand_num = random.randint(1,m-1)
      y = pow(rand_num, t, m)
      prime = False

      if (y == 1):
          prime = True


      for i in range(0,s):
          if (y == m-1):
              prime = True
              break
          else:
              y = (y*y)%m

      if not prime:
          return False

  return True

