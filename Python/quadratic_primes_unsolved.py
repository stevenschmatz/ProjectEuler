def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def isprime(x):
    for i in range(2, x-1):
        if x % i == 0:
            return False
    else:
        return True

a = primes(100000)
prime_sum, count = 0, 0

max_sum = 0

while prime_sum < 1000000:
	prime_sum += a[count]
	count += 1
	if (prime_sum > 900000) and isprime(prime_sum):
		print prime_sum

def test(n):
    return isprime(prime_sum-sum(a[0:n])), prime_sum-sum(a[0:n])


n = 0
while True:
	if test(n)[0]==True:
		print test(n)[1]
		break
	n += 1
