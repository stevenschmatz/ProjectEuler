f = open("keylog.txt", "r")

keylog_list = []
for keylog in f.read().split('\n'):
	if keylog != '':
		keylog_list.append(int(keylog))

first_digit_list = []
second_digit_list = []
third_digit_list = []

for i in range(len(keylog_list)):
	first_digit_list.append(int(str(keylog_list[i])[0]))
	second_digit_list.append(int(str(keylog_list[i])[1]))
	third_digit_list.append(int(str(keylog_list[i])[2]))

frequency_list_1 = []
frequency_list_2 = []
frequency_list_3 = []
for i in range(10):
	frequency_list_1.append([i,first_digit_list.count(i)/float(len(first_digit_list))])
	frequency_list_2.append([i,second_digit_list.count(i)/float(len(second_digit_list))])
	frequency_list_3.append([i,third_digit_list.count(i)/float(len(third_digit_list))])

def remove_zero_probabilities(digit_list):
	templist = []
	for i in digit_list:
		if i[1]!=0.0:
			templist.append(i)
	return templist

frequency_list_1 = remove_zero_probabilities(frequency_list_1)
frequency_list_2 = remove_zero_probabilities(frequency_list_2)
frequency_list_3 = remove_zero_probabilities(frequency_list_3)

test_list = []

for elem in frequency_list_1:
	test_list.append(elem[0])
for elem in frequency_list_2:
	test_list.append(elem[0])
for elem in frequency_list_3:
	test_list.append(elem[0])

print list(set(test_list))

print frequency_list_1 #736128
print frequency_list_2 #1(2 or 6)893
print frequency_list_3 #908(6 or 2)1

#332 combination: (736)(128)(90) => 7312890 
#323 combination: (736)(12)(908) => 73612908
#233 combination: (73)(126)(908) => 73126908
#233 combination: (73)(1628)(908) => 73162890

