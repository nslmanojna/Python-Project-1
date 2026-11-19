print("Hello, World!")
print("This is a simple Python script.")
print("Let's get started with Python programming!")
print("To check if Python is installed on Windows, " \
"search in the start bar for Python or run the following on the Command Line (cmd.exe):")
print("C:\\Users\\Your Name>python --version") 
#Note: Use the Backslash character to print the Backslash character in Python strings.

print("If Python is installed, you will see the version number printed on the screen.")
print("If Python is not installed, you will see an error message.")
print("If Python is not installed on your computer, " \
"you can download it for free from the official website: https://www.python.org/")

print("Python Quickstart")
print("To run Python code, you can use the Python interpreter or an Integrated Development Environment (IDE).")
print("The Python interpreter can be run from the command line, or from an IDE such as " \
"Thonny, Pycharm, Netbeans or Eclipse.")
print("To run Python code from the command line, open a terminal or command prompt and type 'python' " \
"followed by the name of the Python file you want to run. For example:")
print("C:\\Users\\Your Name>python my_script.py")
print("To run Python code from an IDE, open the IDE and create a new Python file. " \
"Then, write your Python code in the file and click the 'Run' button to execute the code.")

print("Python is an interpreted programming language, this means that as a developer you write Python (.py) " \
"files in a text editor and then put those files into the python interpreter to be executed." \
"Let's write our first Python file, called hello.py, which can be done in any text editor:")

#hello.py file content
print("Hello, World!")
print("Save your file. Open your command line, navigate to the directory where you saved your file, and run:")
print("C:\\Users\\Your Name>python hello.py") 
print("Output: Hello, World!")

#To check the Python version of the editor, you can find it by importing the sys module:
import sys

print(sys.version)