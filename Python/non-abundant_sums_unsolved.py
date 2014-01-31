import math

def FindAllDivisors(x):
    divList = []
    y = 1
    while y <= math.sqrt(x):
        if x % y == 0:
            divList.append(y)
            divList.append(int(x / y))
        y += 1
    return divList

def isAbundant(n):
    return sum(FindAllDivisors(n))-n>n

abundantList = []
for i in range(2000):
    if isAbundant(i):
        abundantList.append(i)

abundantSums = []
for i in abundantList:
    for k in abundantList:
        suma = i + k
        if isAbundant(suma):
            abundantSums.append(suma)

print sum([x for x in range(max(abundantSums)) if x not in abundantSums])