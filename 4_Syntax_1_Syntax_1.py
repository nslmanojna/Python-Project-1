#Python Indentation
print("Indentation refers to the spaces at the beginning of a code line.")
print("Where in other programming languages " \
"the indentation in code is for readability only, " \
"the indentation in Python is very important.")
print("Python uses indentation to indicate a block of code.")

if 5 > 2:
  print("Five is greater than two!")

#Python Indentation Error
#If you skip the indentation, Python will give you an error:
# if 5 > 2:
# print("Five is greater than two!")#IndentationError: expected an indented block after 'if' statement on line 13

print("Python Indentation: The number of spaces is up to you as a programmer, " \
"the most common use is four, but it has to be at least one.")

if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!")

print("You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:")
# if 5 > 2:
#  print("Five is greater than two!")
#         print("Five is greater than two!")#IndentationError: unexpected indent

#Python Variables
#In Python, a variable is created when you assign a value to it:

x = 5
y = "Hello, World!"
z = 3.14
a = True
b = None
c = [1, 2, 3]
d=3+4j
print(x, y, z, a, b, c, d)
print(type(x), type(y), type(z), type(a), type(b), type(c), type(d))

#Comments
#Python has commenting capability for the purpose of in-code documentation.
#Comments start with a #, and Python will render the rest of the line as a comment:
# This is a comment
"""
This is a comment
"""


