from sys import argv
from os.path import exists
#here we'll copy data from a file to another blank file
# first we'll read data of one file to a particular place and then copy it to the blank file

script, from_file, to_file = argv
#now read the from file
fileto_becopied = open(from_file)
text = fileto_becopied.read()

print(" lets check if the destination exists")
print ("destination check %r" % exists(to_file))

writefile = open(to_file,'w')
writefile.write(text)
writefile.close()
fileto_becopied.close()
print("to preview we can open both files so hit RETURN")
input("hit RETURN")

