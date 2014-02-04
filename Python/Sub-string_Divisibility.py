import itertools

digits = ["0", "1,", "2", "3", "4", "5", "6","7","8","9"]

a = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))

#Check if the first three are divisible, then remove all entries with those digits in that position