import math

def getSumOfDigitsFactorial(num):
  return sum(map(math.factorial, map(int,str(num))))

def test(num):
	return getSumOfDigitsFactorial(num)==num

def solution(max):
	the_sum = 0
	for i in range(3, max):
		if getSumOfDigitsFactorial(i)==i:
			the_sum += i
	return the_sum

print solution(100000)