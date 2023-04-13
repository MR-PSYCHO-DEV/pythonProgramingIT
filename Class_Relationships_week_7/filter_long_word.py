# Write a Python function to return the list of words that are longer than n from a given list of words
def filter_long_word(list, number):
    return [word for word in list if len(word) > number]


print(filter_long_word("The quick brown fox jumps over the lazy dog".split(), 4))
print(filter_long_word("The quick brown fox jumps over the lazy dog".split(), 3))
print(filter_long_word("The quick brown fox jumps over the lazy dog".split(), 2))
