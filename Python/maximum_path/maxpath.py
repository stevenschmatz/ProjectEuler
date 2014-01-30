import random

class MaximumPath:
	"""Problem 18 of Project Euler"""
	
	def Import_Paths(self):
		f = open('paths.txt',"r")
		self.row_string_list_raw = f.read().split('\n')
		f.close()

	def Create_Path_Array(self):
		self.path_array = []
		for row in self.row_string_list_raw:
			row_list = []
			for number in row.split(' '):
				row_list.append(int(number))
			self.path_array.append(row_list)

	def Generate_Random_Binary(self):
		return random.choice([0,1])

	def Try_Path(self):
		temp_solution = self.path_array[0][0] #75 is always required
		tree_index = 0
		for row in self.path_array[1:]:
			#chooses a path by deciding between two daughter numbers in each row.
			tree_index += self.Generate_Random_Binary()
			temp_solution += row[tree_index]
		return temp_solution

	def Random_Method(self, iterations=100):
		self.solution = 0
		for i in range(iterations):
			pocket = self.Try_Path()
			if pocket > self.solution:
				self.solution = pocket

	def Solve(self):
		self.Import_Paths()
		self.Create_Path_Array()
		self.Try_Path()
		self.Random_Method(iterations=50000)
		print "The maximum path sum is {0}.".format(self.solution)

MySolution = MaximumPath()
MySolution.Solve()
