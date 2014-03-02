import itertools

count = 0
for x in itertools.permutations([1,2,3,4,5,6,7,8,9]):
	count += 1

def is_pandigital(n):
	digit_list = range(10)
	digit_list = digit_list[:len(str(n))]
	for i in range(len(str(n))):
		digit = map(int, list(str(n)))[i]
		if digit not in digit_list:
			return False
		digit_list.remove(digit)
	return True

for i in range(10000):
	is_pandigital(987654321)

print len(set(list(str(323))))