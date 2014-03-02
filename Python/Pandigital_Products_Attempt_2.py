import itertools


def is_pandigital(n):
	length = len(str(n))
	digit_list = range(10)
	digit_list = digit_list[1:length+1]
	if len(set(list(str(n)))) != length:
		return False
	for i in range(length):
		digit = map(int, list(str(n)))[i]
		if digit not in digit_list:
			return False
		digit_list.remove(digit)
	return True

def pandigital_product_q(a, b):
	return is_pandigital(int(str(a)+str(b)+str(a*b)))

pan_count = 0
product_sum = 0
for a in range(1, 5000):
	for b in range(a, 5000):
		if len(set(list(str(a))+list(str(b)))) != len(list(str(a))+list(str(b))):
			continue
		if pandigital_product_q(a, b):
			product_sum += a * b

print product_sum

#for i in range(count):
#	is_pandigital(12342043)