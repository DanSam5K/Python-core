# Namespaces is container that holds names (variables, functions, classes etc)
# Help avoid conflict
# When a module is imported namespace is created where the particular module names recide
# Namespaces Helps different between function and variables with same names from different modules.

from module import print_area

def my_func():
    print("I am here for sure")

if __name__ == "__main__":
    print("I am runing")
    my_func()
    print_area()
    