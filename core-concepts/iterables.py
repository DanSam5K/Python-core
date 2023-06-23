# Object that can be iterated over
# They represent a sequence of elements 
# They can be used in a `for` loop or other iterable operation
# Examples include  list Tuples, strings, and dictionary
# Must implement the `__iter__()` method, which returns an iterator

my_list = [1,2,3]
for item in my_list:
    print(item)