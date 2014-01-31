coins = [1, 2, 5, 10, 20, 50, 100, 200]

TARGET=200

matrix = {}
for y in xrange(0, TARGET+1):
    matrix[y, 0] = 1  # same as matrix[(y,0)]=1

for y in xrange(0, TARGET+1):
    for x in xrange(1, len(coins)):
        matrix[y, x] = 0
        if y>=coins[x]:
            matrix[y, x] += matrix[y, x-1]
            matrix[y, x] += matrix[y-coins[x], x]
        else:
            matrix[y, x] = matrix[y, x-1]

print matrix[y,x],