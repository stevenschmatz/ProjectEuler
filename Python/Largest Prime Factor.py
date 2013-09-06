def primeQ(n):
	o = n
	i = 2
	while i * i < n:
	     while n % i == 0:
	         n = n / i
	     i = i + 1
	return (n == o)

def primeQ2(n):
	i = 2
	list = []
	while i < n:
		if n % i == 0:
			list.append(i)
		i += 1
	if len(list)==0:
		return True
	return False


print 5000000/0.2