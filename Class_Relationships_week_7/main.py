

# Write a Python function that takes two lists and returns True if they have at least one common member
def common_member(listA, listB):
    if len(set(listA).intersection(listB)) >= 1:
        return True
    else:
        return False


# true because there is 4 in the in both
print(common_member([1, 2, 3, 4], [4, 5, 6, 7, 8]))
# true because there is 3 and 4 in the in both
print(common_member([1, 2, 3, 4], [3, 4, 5, 6, 7]))
# false because there are not common members
print(common_member([1, 2, 3, 4], [5, 6, 7, 8, 9]))


# Write a Python function to return the list of words that are longer than n from a given list of words
def filterlongword(list, number):
    return [word for word in list if len(word) > number]


print(filterlongword("The quick brown fox jumps over the lazy dog".split(), 4))
print(filterlongword("The quick brown fox jumps over the lazy dog".split(), 3))
print(filterlongword("The quick brown fox jumps over the lazy dog".split(), 2))
