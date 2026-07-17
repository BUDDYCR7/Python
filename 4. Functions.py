def enter(): # "()" Parentheses", Used for parameter. ":" Colon tells Python a block starts here.
    c = input ("Wellcome: ")
    print ("Hi", c)
enter()


# Calling a Function
def greet():
    print("Hello")
greet() # Calling a Function.


# Use parameter names. Advantages:- More readable, Order doesn't matter, Easier for large functions.
def employee(name, salary, department): # Defining a function. "employee" Function name, choose a meaningful name.
    print(name)
    print(salary)
    print(department)
employee(department="IT", salary=50000, name="Shivam") # Parameter names. Function called.


def add():
    a = int (input ("Enter the first number: "))
    b = int (input ("Enter the second number: "))
    print(a+b)
    print(a*b)
    print(a-b)
    print(a/b)
    print(a%b)
add()


def sum (a, b):
    s =a+b
    return s
print (sum(27,69))
print (sum(2978,3876))
print (sum(265,399))
print (sum(88,1))
print (sum(7654,89))
print (sum(266,898))
print (sum(2,76))


def add (a, b):
    result = a + b
    print(result)

add(13, 2)


# **kwargs
def student(**details):
    print(details)
student(name="Shivam", age=22)


# **kwargs
def student(**details):
    for key, value in details.items():
        print(key, value)
student(name="Shivam", age=22,city="Mumbai",phone=9876543210)


# Positional
def add(a, b):
    return a + b
# Keyword
def student(name, age):
    print(name, age)
# Default
def greet(name, country="India"):
    print(name, country)
# *args
def total(*nums):
    print(sum(nums))
# **kwargs
def profile(**data):
    for key, value in data.items():
        print(key, ":", value)


# My Practice Solution.

# Positional Arguments.
# Create a function introduce(name, age),
# Call the function using positional arguments.
def introduce(name, age):
    print (name)
    print (age)
    
introduce("Shivam",22)


# Keyword Arguments.
# Create a function student(name, course),
# Call it using keyword arguments.
def student(name, course):
    print ("Name:", name)
    print ("Course:", course)
    
student(name = "Shivam", course = "Python")


# Default Arguments
# Create a function, greet(name, message="Good Morning")
def greet (name, message="Good Morning"):
    print (name, message)
    
greet ("Shivam" ",")

# Default Arguments, Override the default.
# Create a function, greet(name, message="Good Morning")
# Override the default
def greet (name, message="Good Morning"):
    print (name, message)
    
greet ("Shivam" ",")
greet ("Imran"+",", "Good Night")





















def calcute_age():
    age = 18
    if age >= 18:
        print ("Adult")
    else:
        print ("Minor")
calcute_age()


def mark_sheet(english, math, hindi):
    print (english)
    print (math)
    print (hindi)
mark_sheet(english = 789, math = 499, hindi = 148)


# Write a function greet(name) that returns:
def greet(name):
    print ("Hello", name)
greet(name = "Alice")


# Write a function square(n) that returns the square of a number.
def square():
    side = int (input("Enter the Number: "))
    print (side * side)
square()


# Write a function add(a, b) that returns the sum of two numbers.
def add(a,b):
    print (a+b)
add(a=4, b=4)


# Write a function is_even(n) that returns True if the number is even, otherwise False.
def even():
    a = int (input("Enter the Number: "))
    if a % 2 == 0:
        print ("EVEN")
    else:
        print ("ODD")
even()


def pattern():
    print ("-"*30)
    
print ("Menu")
pattern()
print ("End")
pattern()