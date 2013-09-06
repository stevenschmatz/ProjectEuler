def fibonacci(n):
	if n < 2:
		return n
	return fibonacci(n-2) + fibonacci(n-1)

for x in range(100):
	if fibonacci(x) > 4000000:
		upperlimit = x - 1
		break

count = 0
for x in range(upperlimit):
	count += fibonacci(x-1)

print count