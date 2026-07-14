a = input ("First Name: ")
print ("length of the word is: ", len(a))

b = ("i have 100$, and i paid 50$ to shiv, 20$ to imran, and 10$ to shashank, how much do i have now")
print (b. count("$"))


# Grade students based on marks.
marks = int (input("Enter the marks: "))

if(marks >= 90):
    Grade = "A"
elif(marks >= 80 and marks < 90):
    Grade = "B"
elif(marks >= 70 and marks < 80):
    Grade = "C"
else:
    Grade = "D"

print ("grade of the student ", Grade)


# Nesting
age = 20
# nesting
if (age >= 55):
    if (age >= 11):
        print ("cannot drive")
    else:
        print ("can drive")
else:
    print ("cannot drive")

a = 'shivam'
print (type (a))

name = "Shivam"
age = 22
course = "Python Course"
status = "Learning Stage"

print ("My name is:",name)
print ("I am:",age)
print ("I am doing:", course)
print ("Currently i am in a:", status)

# Relational/Comparision Operator
a = 1
b = 5
print (a==b)

# Assignment Operator
x=4
x*=27
print (x)

# Identity Operator
c=50
d=90
print (c is not d)

h = "hello"
print (h [1:4])

age = 17

if (age >=18):
    print ("Eligible for Vote")
else:
    print ("Not Eligible for Vote")

list = [2,3,4,5,6,7,]
print (10 not in list)

i = 22
print (22 is i)