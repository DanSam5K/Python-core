# Provide sequence of values at a time
# They use the `__next__()` mehtod to retrieve the next value in the seqeunce
# keep record(track) of their internal state and remember the next value to be returned
# They are created from iterables by calling `iter()` function

my_iterable = [1,2,3]
my_iterator = iter(my_iterable)
print(next(my_iterator)) # 1
print(next(my_iterator)) # 2
print(next(my_iterator)) # 3
print(next(my_iterator)) # StopIterator error will be thrown