# Dunder methods double (__)
# Also known as magic methods or special methods
# Pedefined with double (__)
# Examples (`__init__`, `__iter__`, `__next__`).
# Provide a way to define the behaviour of objects and enable certain language feature
# Like `__iter__` and `__next__` are dunder methods used to implement iterators

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0


    def __iter__(self):
        return self


    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        item = self.data[self.index]
        self.index += 1
        return item

my_iterable = MyIterator([1,2,3])

print(next(my_iterable))
print(next(my_iterable))