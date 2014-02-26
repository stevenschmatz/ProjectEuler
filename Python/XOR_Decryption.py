class Solution:
	def __init__(self):
		import binascii
		f = open('cipher1.txt')
		file_text = f.read()
		self.char_list = file_text.split(',')
		self.letters = list('abcdefghijklmnopqrstuvwxyz')
	
	def Get_Ascii_Value(self, char):
		return int(format(ord(char))) #"a" = 97, "z" = 122

	def Get_Key_Range(self):
		self.key_range = self.Get_Ascii_Value('a')-self.Get_Ascii_Value('z')

	def Get_All_Keys(self):
		self.keys = []
		for key_1 in self.letters:
			for key_2 in self.letters:
				for key_3 in self.letters:
					self.keys.append(key_1+key_2+key_3)

	def Decrypt(self, key):
		decoded_char_list = []
		for i in range(len(self.char_list)):
			if i % 3 == 0:
				decoded_char_list.append(int(self.char_list[i])^self.Get_Ascii_Value(key[0]))
			elif i % 3 == 1:
				decoded_char_list.append(int(self.char_list[i])^self.Get_Ascii_Value(key[1]))
			elif i % 3 == 2:
				decoded_char_list.append(int(self.char_list[i])^self.Get_Ascii_Value(key[2]))
		return ''.join(chr(x) for x in decoded_char_list)

	def Solve(self):
		self.Get_All_Keys()
		for i in range(len(self.keys)):
			words = self.Decrypt(self.keys[i])
			if 'the ' in words and 'a ' in words:
				solution_key = self.keys[i]
		print "The solution to this problem is {0}.".format(sum(map(ord, list(self.Decrypt(solution_key)))))

MySolution = Solution()
MySolution.Solve()