def f(x):
	count = 0
	for n in range(x):
		if n%3 == 0 or n%5 == 0:
			count += n
	return count

print f(1000)