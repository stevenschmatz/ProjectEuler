import math
from fractions import Fraction

def sqrt_2_approximation(depth):
	i = 1
	my_frac = 1 + Fraction(1, 2)
	while i < depth:
		my_frac = 1 + Fraction(1, 2 + (my_frac - 1))
		i += 1
	return my_frac

print sqrt_2_approximation(5)
