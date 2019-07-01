print("EXERCISE 15: READING FILES")
from sys import argv
script, filename = argv
txt = open(filename)
print("here's your file %r" %filename)
print (txt.read())
print("Type the filename again")
file_again = input("enter the filename")
txt_again = open(file_again)

k = txt_again.read()
print(k)

# so to open a filename frst wew have to assign some variable k = open(nameofthefile) then we have to read the values stored in the variable via j = k.read
#print j
