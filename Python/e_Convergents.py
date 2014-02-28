import math
from fractions import Fraction


def sqrt_2_approximation(depth):
	i = 1
	my_frac = 1 + Fraction(1, 2)
	while i < depth:
		my_frac = 1 + Fraction(1, 2 + (my_frac - 1))
		i += 1
	return my_frac

def sqrt_3_approximation(depth):
	i = 1
	my_frac = 1 + Fraction(1, 1)
	while i < depth:
		my_frac = 1 + Fraction(1, 2 - ((i+1)%2) + (my_frac - 1))
		i += 1
	return my_frac

def sqrt_23_approximation(depth):
	i = 1
	numerator_initial = 4
	denom_list = [1,3,1,8]
	my_frac = numerator_initial + Fraction(1, denom_list[0])
	while i < depth:
		my_frac = numerator_initial + Fraction (1, denom_list[(i-1)%4] + (my_frac - numerator_initial))
		i += 1
	return my_frac

def generate_e_list(depth):
	my_list = []
	for i in range(depth):
		if i%3 == 1:
			my_list.append((i/3)*2 + 2)
		else: 
			my_list.append(1)
	return my_list

def generate_e_convergence(depth):
	if depth == 1:
		return 2
	depth -= 1
	test_list = generate_e_list(depth) # [1, 2, 1, 1, 4, 1]
	index = depth - 1 # 5
	my_frac = Fraction(1, test_list[index])
	while index > 0:
		index -= 1
		my_frac = Fraction(1, test_list[index] + my_frac)
	return my_frac + 2

numerator = generate_e_convergence(100).numerator

print sum(map(int, list(str(numerator))))


