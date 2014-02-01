def modular_pow(base, exponent, modulus): #runtime O(e)
    c = 1
    for i in range(exponent):
        c = (c * base) % modulus
    return c



def Get_Count(n):
	count = 0
	x = 2
	while x<n:
		a = modular_pow(x, 3, n)
		if a == 1:
			count += 1
			print x
		x += 1
	return count

print Get_Count(2300234)