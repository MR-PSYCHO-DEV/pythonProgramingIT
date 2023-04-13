from random import shuffle

listA = "The quick brown fox jumps over the lazy dog".split()
listA.sort()
listB = [1, 2, 3, 4, 5, 6, 7, 8, 9]


shuffle(listA)
shuffle(listB)


print(listA)
print(listB)
