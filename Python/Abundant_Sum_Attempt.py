import math


maximum = 4000

def Generate_Divisors(n):
    large_divisors = []
    for i in xrange(2, int(math.sqrt(n)+1)):
        if n % i is 0:
            yield i
            if i is not n / i:
                large_divisors.insert(0, n / i)
    for divisor in large_divisors:
        yield divisor

def Get_Divisor_Sum(n):
    return sum(list(Generate_Divisors(n)))

def Is_Abundant(n):
    return Get_Divisor_Sum(n) > n

def Get_All_Abundant_Nums(max):
    abundant_list = []
    for i in range(max):
        if Is_Abundant(i):
            abundant_list.append(i)
    return abundant_list

abundant_list = Get_All_Abundant_Nums(maximum/2)

listtt = [x for x in range(maximum)]
for i in abundant_list:
    for j in abundant_list:
        summ = i + j 
        if summ in listtt:
            listtt.remove(summ)

print sum(listtt)



