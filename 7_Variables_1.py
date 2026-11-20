#Variables
# Variables are containers for storing data values.
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
#Variables do not need to be declared with any particular type, 
#and can even change type after they have been set.

x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int 
x = "Sally" # x is now of type str
print(x) #Output: Sally

#Casting: If you want to specify the data type of a variable, 
# this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Type of variable: You can get the data type of a variable 
#with the type() function.

print(type(x)) #Output: <class 'str'>
print(type(y)) #Output: <class 'int'>
print(type(z)) #Output: <class 'float'>

#Variable names: Variable names are case-sensitive.
# A variable can have a short name (like x and y) or a 
# more descriptive name (age, carname, total_volume). 
# Rules for Python variables:
# A variable name must start with a letter or the underscore character 
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters 
# and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive(age, Age and AGE are three different variables)
