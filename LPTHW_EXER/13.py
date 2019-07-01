# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 08:35:03 2019

@author: Pranav
"""

# EXERCISE 13 (PARAMETERS, UNPACKING AND VARIABLES

#from sys import argv
#script, first, second, third = argv
#the line above unpacks the variables assigned rather than hoding the argumrnts 
#it gets assigned to four variables and "TAKE WHATEVERS IN THE ARGV AND UNPACK IT AND ASSIGN IT TO THE VARIABLES"
#print"the script is called", script
#print "this is your firt variable", first
#print"your second variable is ", second
#print"your third variable is ", third
#the argv is the argument varibale you pass to tne 
#python script the argv is argument varibale a very standard name im programming thay you'll find in many languages

#EXERCISE 14 PROMPTING AND PASSING
from sys import argv
script, user_name, ewww = argv
prompt ='HUH?'

print "Hi! %s thos is %s script" % (user_name,script)
print "I'd like to ask you a few questions."
print"DO you like me %s" % user_name
likes = raw_input('prompt')

print"where do you live %s, %s i judge you" % (user_name, ewww)

lives = raw_input('prompt')
print"what kinda rig do you have?"
computer = raw_input(prompt)

print """

Alright so now you've declared that %r abput liking me
you live in %r. Not sure where that is,
and you have a %r computer... naaaice!!!
"""% (likes, lives, computer)

