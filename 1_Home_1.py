#Print Syntax 1 - Using end parameter
print("Python is a popular programming language.", end='')
print("Python can be used on a server to create web applications.", end='')
print("Python is easy to learn.")

#Print Syntax 2 - Each print statement on a new line
print("Python is a popular programming language.")
print("Python can be used on a server to create web applications.")
print("Python is easy to learn.")

#Print Syntax 3 - Using backslash to continue the statement on the next line, 
#and using end parameter to avoid new line after each print statement, 
#and using semicolon to separate the print statements on the same line
print("Python is a popular programming language.", end=''); print("Python " \
"can be used on a server to create web applications.", end=''); print("Python "
"is easy to learn.")

#Print Syntax 4 error
# print("Python is a popular programming language.") print("Python is easy to learn.")
#SyntaxError: invalid syntax. Did you mean 'in'?
#Note:The above code will throw an error because there is no semicolon or newline separating the two print statements.

print("Hello, World!")

# Download Python
# Download Python from the official Python web site: https://python.org

#Practice Programs
#Print your name
name = "John Doe"
print("My name is", name)

#Add two numbers
a=10
b=20
print("The sum of a and b is:", a + b)

#Find square of a number
number=int(input("Enter a number: "))
square=number*number
print("The square of", number, "is", square)

#Simple calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
#Addition
sum = num1 + num2
print("Sum is: ", sum)
#Subtraction
difference = num1 - num2
print("Difference is: ", difference)
#Multiplication
product = num1 * num2
print("Product is: ", product)
#Division
division = num1 / num2

if num2 != 0:
    division = num1 / num2
    print("Division is: ", division)
else:
    print("Error: Division by zero is not allowed.")