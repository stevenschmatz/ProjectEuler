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
		my_frac = numerator_initial + Fraction (1, denom_list[(i-1)%4] + (my_frac - 4))
		i += 1
	return my_frac

print float(sqrt_23_approximation(100)) - math.sqrt(23)
