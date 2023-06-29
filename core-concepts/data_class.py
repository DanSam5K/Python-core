# Provide decorators and set of tools to automatically generate boilerplate code for creating datac lasses
# Classess used store data and have attribute no cmplx behv or method
# Commonly used to store structure data like config, db records or simple data containers
# used `@dataclass` provided by dc module
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    z: float

# Create instances of the point class
p1 = Point(1.0, 2.0, 3.0)
p2 = Point(4.0, 5.0, 6.0)

# Access and modify attibutes
print( p1.x, p1.y, p1.z)

p1.x, p1.y, p1.z = 10.0, 20.0, 30.0

print( p1.x, p1.y, p1.z)


@dataclass
class Person:
    name: str
    age: int = 0  # Default value specified

p1 = Person("Alice")
print(p1)  # Output: Person(name='Alice', age=0)

p2 = Person("Bob", 25)
print(p2)  # Output: Person(name='Bob', age=25)

@dataclass(frozen=True)
class Point:
    x: float
    y: float

p = Point(1.0, 2.0)
# print(p.x + p.y)  # Output: 3.0

p.x = "hello"  # Type hint violation, may be caught by a type checker
