def Primes(n):
    if n == 2:
        return [2]
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n /= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac


def Four_Divisors(n):
    return len(list(set(primes(n))))==4

def Solve():
    i = 0
    count = 1
    previous = 0
    while True:
        if four_divisors(i):
            if i-previous == 1:
                count += 1
            else:
                count = 1
            previous = i
        if count == 4:
            return i-3
            break
        i += 1

print Solve() #returns 134043
