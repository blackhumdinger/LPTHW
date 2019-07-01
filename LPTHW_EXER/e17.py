print("EXERCISE 17 MORE FILES")
from sys import argv 
from os.path import exists
script, from_file, to_file =argv
print("copying from %s to %s" % (from_file, to_file))
# we could do these on one line too//\
infile = open(from_file)
indata = infile.read()

print(" the input file is %d bytes long" % len(indata))

print(" does the output file exist?? %r" % exists(to_file))
print("ready??, hit RETURN to continue and to stop press CTRL+C")
input("press button")
out_file = open(to_file,'w')
out_file.write(indata)
print("alright! we're done here")

out_file.close()
infile.close()

print(" to preview lets open the other file and check if you want to you can extend the code and do it")