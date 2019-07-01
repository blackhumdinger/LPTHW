from sys import argv
print("EXERCISE 14 PROMPTING AND PASSING")
script, username =argv

prompt = '>'

print ("Hi %s I'm the %s script." % (username, script))
print("I'd like to ask you a few questions")
print("do you like me %s" % username)
likes= input(prompt)
print("where do you live")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print( """Alright, so you say %r about liking me.
you live in %r ,
 and you have a %r """ % (likes, lives, computer)) 