# AND operator
print("True and True is", True and True)
print("True and False is", True and False)
print("False and True is", False and True)
print("False and False is", False and False)

# OR operator
print("True or True is", True or True)
print("True or False is", True or False)
print("False or True is", False or True)
print("False or False is", False or False)

print("Not Operator")
a = not(True)
print(a)
print(type(a))

a = input("Enter number 1: ")
b = input("Enter number 2: ")
print("Number 1 is:", a)
print("Number 2 is:", b)
print("Sum is: ", a+b) #Returns in string

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
print("Number 1 is:", a)
print("Number 2 is:", b)
print("Sum is: ", a+b) #Returns in int

a = int(input("Enter any number: "))
print("The sqaure of this number is with power:", a**2)
print("The sqaure of this number is without power:", a*a)