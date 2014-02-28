from operator import mul

limit = 28123

def factorization(n):
    p = 1
    while p * p < n:
        p += 1
        k = 0
        while n % p == 0:
            k += 1
            n //= p
        if k:
            yield p, k
    if n != 1:
        yield n, 1

def sum_of_divisors(n):
    return reduce(mul, ((p**(k+1)-1) // (p-1) for p, k in factorization(n)), 1) - n

def is_abundant(n):
	if n % 60 == 0:
		return True
	return sum_of_divisors(n) > n

abundant_list = [num for num in range(2, limit) if is_abundant(num)]

abundant_sums = []

for i in abundant_list:
	for j in abundant_list:
		if i + j <= limit:
			abundant_sums.append(i + j)
		else:
			break


print reduce(lambda x, y: x + y, range(limit+1)) - sum(list(set(abundant_sums)))