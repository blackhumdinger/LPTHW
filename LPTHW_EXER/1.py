# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 10:56:19 2019

@author: Pranav
"""

#EXERCISE 2
#COMMENTS ARE IMPORTANT IN PYTHON THEY ARE USED TO TEMPORARILY DISABLE THE CODE SNIPPET IF WE NEED NOT USE IT RIGHT N
#print "hello there!!"
#print "we're gonna do this"
#print "hell yeah!!1"
#print "yaaay!!! its printing!!!"


#EXERCISE 3
print "i will now count my chickens"#SIMPLE PRINTING
print"hens", 25+30/6 #PRINTING AND THEN DISPLAYING THE ARITHMETIC RESULT
print"roosters",100-25*3%4#SAME AS ABOVE
print"now i will count the number of eggs"
print 3+2+1-5+4%2-1/4+6 #PRINTS THE ARITHMETIC RESULT

print "is it true that 3+2<5-7"
print 3+2<5-7 #WHEN COMPARISON OPERATORS ARE USED THE TRUE OR FALSE IS GIVEN OUT INDICATING THAT THE CONDITION IS TRUE OR FALSE
print"what is 3+2", 3+2 #PRINTS THE SENTENCE AND THE RESULT OF THE CODE GIVEN
print"what is 5-7", 5-7
print"oh!, thats why its false"
print"how about some more"
print"is it greater",5>-2 #COMPARIOSN 
print"is it greater than or equal",5>=2#COMPARISON
print"is it less than or equal to",5<=2#COMPARISON
#IF WE GIVE MATHEMATICAL CONDITIONS FOR THE CODE IT WOULD RETURN A TRUE OR FALSE AS THE VALUE OF THE COMPARISON
 #IN CASE WE NEED FLOATING POINTS THEN WE CAN USE A DECIMAL AFTER THE NUMBER SO THE COMPILER CAN DISTINGUISH ITSELF AS A FLOAT RATHER THAN AN INTEGER 
 
 
print"------------------------------------------------------"
 #ORDER OF OPERATIONS IS PEMDAS
 
 
 #EXERCISE 4
 #VARIABLES AND NAMES
cars=100
space_in_a_car =4.0
drivers = 30
passengers = 90
cars_not_driven = cars -drivers

cars_driven =drivers 
carpool_capacity = cars_driven *space_in_a_car
average_passengers = passengers/cars_driven 
print"there are", cars, "cars available"
print"there are only",drivers,"drivers available"
print"we can transport",carpool_capacity,"people today"
print"there are",cars_not_driven,"empty cars"
print"we have",passengers,"to carpool today"
print"we need to put about ",average_passengers,"in each car"
#ANSWERS TO EXERCISES
#!. THE CAR_POOL IS THE CULPRIT WE NEED CARPOOL_CAPACITY AS THE VARIABLE THERES A TYPOGRAPHIC ERROR IN THE CODE
#2. WE CAN USE FLOATING TYPE NUMBERS TO MAKE CALCULATIONS IN DECIMAL PLACES
#SINGLE EQUALS TO IS ASSIGNMENTS AND DOUBLE EQUALS TO CHECKS IF BOTH HAVE THE SAMEINTEGER OR FLOAT VALUE




print"----------------------------------------------------------------------"
#EXERCISE 5 (MORE VARIABLES AND PRINTING)

#LEARNING ABOUT A FORMATTED STRING
my_name = "Chandler M. Bing"
my_age = 35  #i aint lying
my_height = 6.0
my_weight = 180
my_eyes = 'green'
my_teeth = 'white'
my_hair = 'brown'
print"lets talk about %s" % my_name," could i be more funny"
print"hes %d feet tall"% my_height
print"hes %d pounds heavy" % my_weight
print"hes got %s eyes and %s hair"%(my_eyes, my_hair)
print"his teeth are usually %s depending upon the coffee" % my_teeth
print"if i add %d, %d, and %d i get %d"% (my_age, my_height, my_weight, my_age+my_height+my_weight),"*sums it all up huh? xD*"
#Both __str__ and __repr__ functions are very similar. We can get the object representation in String format 
#as well as other specific formats such as tuple and dict to get information about the object.
# __str__ must return string object whereas the __repr__ must return any kind of object in python


print("---------------------------------------------------------------------")
#EXERCISE 6 (STRINGS AND TEXT)
#A STRING IS USUALLY A  BIT OF TEXT YOU WANT TO DISPLAY TO SOMEONE OR "EXPORT
# OUT OF THE PROGRAM YOU ARE WRITING STRINGS HAVE DOUBLE OR SINGLE QUOTES WRAPPED AROUD THEM
#IF WE NEED TO FORMAT MULTIPLE STRINGS THEN WE MUST MERGE THEM IN A PARENTHESIS AND 
# WE SHOULD FORMAT THEM IN A COMBINATION LIKE % (AGE, ROLL_NO , SALARY)
x = "there are %d types of people"% 10
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s"% (binary,do_not)

print x
print y

print"i said: %r" % x
print"i also said: '%s'." %y

hilarious = False
joke_evaluation = "isnt that joke funny? %r"
print joke_evaluation % hilarious
w = "this is the left side of the string..."
e = "this is the right side of the string"
print w+e
#%r is good for debugging the others are used to display the output to the users



print("---------------------------------------------------------------------")
#EXERCISE 7 (MORE PRINTING)


print ("mary had a little lamb")
print("its fleece was white as %s")% 'snow'#a variable doesnt have single quotes around it whereas a string does
print("and everywhere that Mary went.")
print " . "*10
end1 = "C"
end2 = "H"
end3 = "E"
end4 = "E"
end5 = "S"
end6 = "E"
end7 = "B"
end8 = "U"
end9 = "R"
end10 = "G"
end11 = "E"
end12 = "R"


print end1+end2+end3+end4+end5+end6,# the comma at the end denotes that the next line would be adjacent rather than a separate one
print end7+end8+end9+end10+end11+end12
# in python a string of more than 80 characters is said to be bad practice

print"*"*40
#EXERCISE 8 {PRINTING PRINTING}
formatter = "%r %r %r %r"
print formatter%(1,2,3,4)
print formatter%("uno","dos","tres","hala madrid!")
print formatter%(formatter, formatter, formatter, formatter)
print formatter%("i had this thing",
                 "That you could type right",
                 "but it didnt sing",
                 "so i said goodnight!")
print"*"*40
#EXERCISE 9 (PRINTING PRINTING PRINTING)
days ="mon tue wed thu fri sat sun"
months = "\njan\n feb\n mar\n april \n may\n june \n jul\n aug\n sep\n oct\n nov\n dec\n"
print"here are the days %s" % days
print"here are the months %s" % months
print """  
here's something new 
we can type as long as we want by this method of 
you know triple quotes its clearly visible duh!
any number of lines 3 4 or 5 we dont care
 """ # these are used in case we need to print the double quotes or single quotes 
 #in a statement and the backlash sequences are used to put difficult to type characters in a string
tabby_cat = "\tI'm tabbed in."
persian_cat = "i'm split on \n line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat="""
I'll do a list:
  \t* cat food
  \t* fishes
  \t* catnip\n\t* grass

"""
print tabby_cat
print persian_cat 
print backslash_cat
print fat_cat

print"*"*40
#while True:
 # for i in ("/","-","|","\\","|"):
  
#  print"%s\r" %i,
  #  INSTAGRAM MOVIE REVIEW
  # EXERCISE 11 (aSKING QUESTIONS)
  # TAKE IN AN INPUT
  # CHANGE IT
  # PRINT OUT SOMETHING TO SHOW HOW IT CHANGED
  
print("how old are you?")
age = raw_input()
print("what is your name")
name = raw_input()
print("what is your height")
height = raw_input()
print("so you are %r old, %r tall and %r heavy") %(age,name,height)
# RAW INPUT PRINTS OR GIVES THE DATA AWAY IN A STRING FORMAT RATHER THAN INTEGER IF THE INPUT IS OF TYPE INTEGER
# INPUT() FUNCTION CONVERTS THE INPUT CODE AS IF IT WERE SOME PYTHON CODE WHEREAS THE RAW_INPUT() FUNCTION TAKES IN THE ARGUMENT AS IT IS
# If the prompt argument is present, it is written to
# standard output without a trailing newline.
# The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that.
# When EOF is read, EOFError is raised. Example:

print("*"*40)
age = raw_input("how old are you?")
height = raw_input("how tall are you?")
weight = raw_input("what is your weight?")
print("so you are %r old, %r tall and %r heavy")


