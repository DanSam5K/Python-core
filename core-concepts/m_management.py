# Reference Counting
x = 32 # Ref countof Int Object 32 increase +1
y = x # ref count increase to 2
x = None # ref count decrease by -1 to 1
y = None # ref count decrease to 0, and object is garbage collected

# Garbage collection(GC) Python uses GC to reclaim memory occupied by objects with zero refs counts
# GC is responsible for identifying and deallocating mem
# GC helps manage circular refs where objects refer to each, preventing mem leaks

# Mem Allocation: Python Memeroy Manager(PMM)
# PMM handles alloc and dealloc mem blocks for objects
# PMM Mangages heaps(large pool of mem wc objects are alloc)
# PMM keeps tracks of available mem blocks and assign them as needed

my_list = [1, 2, 3] # mem alloc of list
my_dict = {'a':1, 'b': 2} # me alloc for dict object
my_list = None # mem is dealloc

# Dereferencing refers to removing ref to an object
# when ref counts reaches zero it is deref
