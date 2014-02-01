def Get_Digits(p):
	digit_list = []
	for digit in list(str(p)):
		digit_list.append(int(digit))
	return digit_list

def iteration(n):
	next_number = 0
	for digit in Get_Digits(n):
		next_number += digit**2
	return next_number

def method(n):
	squares = 0
	for i in range(n):
		k = i
		while k > 1:
			if k == 89:
				squares += 1
				break
			k = iteration(k)
	return squares

print method(10000000) #outputs 8581146
