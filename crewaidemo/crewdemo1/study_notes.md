# Python Basics: A Beginner's Guide

## Introduction to Python

### What/Why
Python is a versatile, high-level programming language known for its readability and ease of use. It's used in web development, data science, machine learning, and more. It has a large and active community.

### Simple Example
After installing Python, you can run your first program:

```python
print("Hello, World!")
```

### Mini Checklist/Tip
*   Make sure Python is installed correctly (check your system's documentation for installation).
*   Use a code editor (like VS Code, Sublime Text, or IDLE) for writing Python code.

## Data Types

### What/Why
Data types classify the type of value a variable can hold. Understanding them is fundamental to Python programming.

*   **int:** Integers (whole numbers). Example: `5`, `-10`.
*   **float:** Floating-point numbers (numbers with decimal points). Example: `3.14`, `-2.5`.
*   **str:** Strings (text). Example: `"hello"`, `"Python"`.
*   **bool:** Booleans (True or False).

### Simple Example
```python
age = 30          # int
price = 19.99     # float
name = "Alice"    # str
is_active = True  # bool

print(type(age)) # Output: <class 'int'>
```

### Mini Checklist/Tip
*   Use the `type()` function to check the data type of a variable.

## Variables and Assignment

### What/Why
Variables store data. Assignment uses the `=` operator to assign a value to a variable.

### Simple Example
```python
name = "Bob"
age = 25
price = 99.99
```

### Mini Checklist/Tip
*   Variable names should start with a letter or underscore.
*   Variable names are case-sensitive (`name` is different from `Name`).
*   Avoid using Python reserved keywords (e.g., `if`, `else`, `for`) as variable names.

## Operators

### What/Why
Operators perform operations on values.

*   **Arithmetic:** `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), `%` (modulo - remainder), `**` (exponentiation).
*   **Comparison:** `==` (equal to), `!=` (not equal to), `>` (greater than), `<` (less than), `>=` (greater than or equal to), `<=` (less than or equal to).
*   **Logical:** `and`, `or`, `not`.

### Simple Example
```python
a = 10
b = 5
sum = a + b         # 15
is_equal = (a == b) # False
is_greater = (a > b)  # True
```

### Mini Checklist/Tip
*   Use parentheses to control the order of operations.

## Input and Output

### What/Why
Input gets data from the user; output displays data to the user.

### Simple Example
```python
name = input("Enter your name: ")
print("Hello, " + name + "!")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = num1 + num2
print("The sum is:", sum)
```

### Mini Checklist/Tip
*   The `input()` function always returns a string. Use `int()`, `float()`, etc., to convert the input to the desired data type.

## Control Flow: Conditional Statements

### What/Why
`if`, `elif`, and `else` statements control the flow of a program based on conditions.

### Simple Example
```python
age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

```python
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")
```

### Mini Checklist/Tip
*   Indentation is crucial. The code block under `if`, `elif`, and `else` must be indented.

## Control Flow: Loops

### What/Why
Loops execute a block of code repeatedly.

*   `for` loops iterate over a sequence (like a list or a range).
*   `while` loops continue as long as a condition is true.

### Simple Example
```python
# for loop
for i in range(5): # Iterates 0, 1, 2, 3, 4
    print(i)

# while loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1
```

### Mini Checklist/Tip
*   Be careful to avoid infinite loops (a loop that never ends).

## Data Structures: Lists

### What/Why
Lists store an ordered collection of items.

### Simple Example
```python
# Creating a list
my_list = [1, 2, 3, "apple", "banana"]

# Accessing elements (index starts at 0)
print(my_list[0])  # Output: 1

# Modifying an element
my_list[0] = 10

# Slicing (getting a portion of the list)
print(my_list[1:3])  # Output: [2, 3]
```

### Mini Checklist/Tip
*   Lists are mutable (changeable).

## Data Structures: Dictionaries

### What/Why
Dictionaries store data in key-value pairs.

### Simple Example
```python
# Creating a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Accessing values
print(my_dict["name"])  # Output: Alice

# Modifying a value
my_dict["age"] = 31

# Adding a new key-value pair
my_dict["occupation"] = "Engineer"
```

### Mini Checklist/Tip
*   Dictionaries are mutable. Keys must be unique and immutable (e.g., strings, numbers).

## Functions

### What/Why
Functions are reusable blocks of code. They help organize code and reduce redundancy.

### Simple Example
```python
def greet(name):  # Function definition
    print("Hello, " + name + "!")

greet("Bob")  # Calling the function
```

```python
def add(x, y):
    return x + y # Function with return value

result = add(5, 3)
print(result)  # Output: 8
```

### Mini Checklist/Tip
*   Use `def` to define a function.
*   Use `return` to send a value back from a function.

## Modules

### What/Why
Modules are files containing Python code.  They allow you to organize code into reusable components.

### Simple Example
```python
import random

# Generate a random integer between 1 and 10
random_number = random.randint(1, 10)
print(random_number)

import math
print(math.sqrt(16)) # Output: 4.0
```

### Mini Checklist/Tip
*   Use `import module_name` to import a module.
*   Use `module_name.function_name()` to call a function from a module.

## String Manipulation

### What/Why
String manipulation involves working with text.

### Simple Example
```python
my_string = "hello world"

# Length
print(len(my_string))  # Output: 11

# Lowercase
print(my_string.lower()) # Output: hello world

# Uppercase
print(my_string.upper()) # Output: HELLO WORLD

# Split
words = my_string.split() # Output: ['hello', 'world']

# Join
joined_string = " ".join(words) # Output: hello world
```

### Mini Checklist/Tip
*   Strings are immutable; string methods create new strings rather than modifying the original.

## File Handling (Basic)

### What/Why
File handling allows you to read from and write to files.

### Simple Example
```python
# Writing to a file
file = open("my_file.txt", "w")  # Open file in write mode
file.write("Hello, file!")
file.close()

# Reading from a file
file = open("my_file.txt", "r") # Open in read mode
content = file.read()
print(content) # Output: Hello, file!
file.close()
```

### Mini Checklist/Tip
*   Always close the file using `file.close()` to release system resources. Use `with open(...) as file:` for automatic closing.

## Error Handling (Basic)

### What/Why
Error handling helps prevent program crashes.

### Simple Example
```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a number.")
```

### Mini Checklist/Tip
*   Use `try` to enclose code that might raise an exception.
*   Use `except` to handle specific exceptions.

## Self-Check

1.  What is the purpose of the `input()` function in Python?
    *   A) To print text to the console.
    *   B) To get input from the user.
    *   C) To define a function.
    *   D) To perform calculations.

2.  Which data type represents whole numbers?
    *   A) `str`
    *   B) `float`
    *   C) `int`
    *   D) `bool`

3.  What does the `==` operator do?
    *   A) Assignment
    *   B) Comparison for equality
    *   C) Addition
    *   D) Subtraction

4.  What keyword is used to define a function in Python?
    *   A) `print`
    *   B) `input`
    *   C) `def`
    *   D) `class`

5.  Which statement is used to handle potential errors in Python?
    *   A) `if`
    *   B) `for`
    *   C) `try`
    *   D) `while`

*Answers: 1: B, 2: C, 3: B, 4: C, 5: C*