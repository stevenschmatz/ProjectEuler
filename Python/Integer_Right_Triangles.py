import math

def Get_B_Bounds(p):
	b_lower_bound = p/(2 + 2**(0.5))
	b_upper_bound = p/2
	return int(math.ceil(b_lower_bound)), b_upper_bound


def Get_Number_Of_Right_Triangles(perimeter):
	lower, upper = Get_B_Bounds(perimeter)
	triangle_count = 0
	for test_B_value in range(lower, upper):
		for i in range(1,lower):
			C_value = (math.sqrt(i**2 + test_B_value**2))
			if (C_value % 1 == 0) and (i + test_B_value + C_value == perimeter):
				triangle_count += 1
	return triangle_count

def Solve(perimeter_maxiumum):
	maximum = 0
	most_triangles = 0
	for perimeter in range(perimeter_maxiumum):
		num_triangles = Get_Number_Of_Right_Triangles(perimeter)
		if num_triangles > maximum:
			maximum = num_triangles
			most_triangles = perimeter
	return most_triangles

print "The perimeter value that gives the maximum number of right triangles is {0}.".format(Solve(1000))
#returns 840