# Is a powerful python library
# commonly used for

# Data validation and parsing
from pydantic import BaseModel, BaseSettings

class User(BaseModel):
    name: str
    age: int

# Parsing and Vlaidation
user_data = {"name": "Daniel", "age": 32}
user = User(**user_data)
print(user.name)
print(user.age)
try:
    user = User(**user_data)
except Exception as e:
    print("Validation error:", e)

invalid_data = {"name": "Samuel", "age": "32"}

try:
    invalid_user = User(**invalid_data)
    invalid_user.age = "15"
except Exception as e:
    print("Validation error:", e)

print(invalid_user.age)

# Configuration Management
class MyConfig(BaseSettings):
    api_key: str
    debug: bool = False

# config = MyConfig()

# config.load_dotenv()
# print(config.api_key)

class Book(BaseModel):
    title: str
    author: str
# Serialization to JSON
# Serialization to JSON
book = Book(title="The Great Gatsby", author="F. Scott Fitzgerald")
json_data = book.json()
print(json_data)  # Output: {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}

# Deserialization from JSON
new_book = Book.parse_raw(json_data)
print(new_book.title)  # Output: The Great Gatsby
print(new_book.author)  # Output: F. Scott Fitzgerald


# Type Hinting and Static Validation
class Rectangle(BaseModel):
    width: float
    height: float

def calculate_area(rectangle: Rectangle) -> float:
    return rectangle.width * rectangle.height

# Static type checking
invalid_rectangle = Rectangle(width=10, height="5")  # Type mismatch, height should be a float
area = calculate_area(invalid_rectangle)  # Type checker will raise an error

# Correct usage
valid_rectangle = Rectangle(width=10.5, height=5.0)
area = calculate_area(valid_rectangle)
print(area)  # Output: 52.5
