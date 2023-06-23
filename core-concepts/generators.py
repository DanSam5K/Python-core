# Generators are a type of iterator that can be defined using special syntax in Python
# They are functions that use the `yield` instead of `return`
# When called it returns an ietrator object
# Allowing one to write iterator in a more concise manner.

def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))