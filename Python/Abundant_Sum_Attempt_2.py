from operator import mul

limit = 2000

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
	return sum_of_divisors(n) > n

abundant_list = [x for x in range(limit/2 + 1) if is_abundant(x)]

abundant_sum_list = []

for num in abundant_list[1:]:
	for num2 in abundant_list[1:]:
		tempsum = num+num2
		if tempsum > limit:
			continue
		if tempsum not in abundant_sum_list:
			abundant_sum_list.append(tempsum)

sum_of_all_numbers = reduce(lambda x, y: x + y, range(limit))
sum_of_abundant_nums = sum(list(set(abundant_sum_list)))

print sum_of_all_numbers - sum_of_abundant_nums