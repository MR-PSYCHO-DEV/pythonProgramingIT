

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
