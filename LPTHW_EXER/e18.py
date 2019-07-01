print("EXRECISE 18: NAMES VARIABLES AND FUNCTIONS")
print(""" the properties of functions can be listed as follows:
1. they name pieces of code the same way variables name strings and numbers
2. they take arguments the same way we pass argv to the script
3. using #1 and #2 we can generate mini pieces of code or tiny commands



""")
from sys import argv
def print_two(*args):
    arg1, arg2 = args
    print ("arg1, %r, arg2, %r" %(arg1, arg2))

def print_two_again(arg1, arg2):
    print("arg1,%r , arg2, %r" %(arg1, arg2))

#ths takes only one argument
 
def print_one(arg1):
    print("this is the only argument %r" %arg1)

def print_none():
    print("nothing!")


print_two("zedd", "shawn")
print_two_again("nicky","skrillex")
print_one("asd")
print_none()
#define is given by def.. 
#on the sanme line as def we give the function name the function name can be anything exceot it should give us the correct functionality 
# *args are lot like argv except they are defined for functions rather than the commandline
# the fucntion ends with a colon and after that we get indentation of 4 spaces 
#to demonstrate how it works we can print these arguments just like in a script

