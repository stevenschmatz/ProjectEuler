import itertools

count = 0
for x in itertools.permutations([1,2,3,4,5,6,7,8,9]):
	count += 1

def is_pandigital(n):
	length = len(str(n))
	digit_list = range(10)
	digit_list = digit_list[:length]
	if len(set(list(str(n)))) != length:
		return False
	for i in range(length):
		digit = map(int, list(str(n)))[i]
		if digit not in digit_list:
			return False
		digit_list.remove(digit)
	return True

for i in range(count):
	is_pandigital(1234)