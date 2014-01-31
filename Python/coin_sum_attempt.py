coins = []

total_value = 10

maximum = 20

a_value = 100
b_value = 50
c_value = 20
d_value = 10
e_value = 5
f_value = 2
g_value = 1

def g_branch(n):
	return 1

def f_branch(n):
	return n/2 + g_branch(n)

def e_branch(n):
	count = 0
	for i in range(1, n/e_value):
		count += f_branch(i*e_value)
	return count

def efg(n):
	return e_branch(n)+f_branch(n) + g_branch(n)

def d_branch(n):
	count = 0
	for i in range(1, n/d_value):
		count += efg(i*d_value)
	return count + 1

def defg(n):
	return d_branch(n)+efg(n)

def c_branch(n):
	count = 0
	for i in range(1, n/c_value):
		count += defg(i*c_value)
	return count + 1

def cdefg(n):
	return c_branch(n) + defg(n)

def b_branch(n):
	count = 0
	for i in range(1, n/b_value):
		count += cdefg(i*b_value)
	return count + 1

def bcdefg(n):
	return b_branch(n)+cdefg(n)

def a_branch(n):
	count = 0
	for i in range(1, n/a_value):
		count += bcdefg(i*a_value)
	return count + 1

def abcdefg(n):
	return a_branch(n)+bcdefg(n)

def solution(n):
	return abcdefg(n)+1

print solution(200)

"""
20,20
20,



"""

