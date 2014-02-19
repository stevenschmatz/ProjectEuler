"""
								Expanded			Secondary diff. 	Tertiary diff.			
Triangle numbers: n(n+1)/2 =	(n^2)/2 + n/2 		1, 2, 3, 4 ... 		1
Pentagonal numbers: n(3n-1)/2 = 3(n^2)/2 - n/2 		1, 4, 7, 10... 		3
Hexagonal numbers: n(2n-1) = 	2(n^2) - n 			1, 5, 9, 13... 		4

"""

def getTriangular(n):
	return n*(n+1)/2

def getPentagonal(n):
	return n*(3*n-1)/2

def getHexagonal(n):
	return n*(2*n-1)

def isTriangular(k):
	n_value = 0.5*(-1+(8*k+1)**(0.5))
	return int(n_value)==n_value

def isPentagonal(k):
	n_value = (1/6.0)*(1+(24*k+1)**(0.5))
	return int(n_value)==n_value

def isHexagonal(k):
	n_value = (1/4.0)*(1+(8*k+1)**(0.5))
	return int(n_value)==n_value

def isTriPentHex(k):
	return (isTriangular(k) and isPentagonal(k) and isHexagonal(k))

i = 0
count = 0
while count < 3:
	if isTriPentHex(getTriangular(i)):
		count += 1
		print getTriangular(i)
	i += 1