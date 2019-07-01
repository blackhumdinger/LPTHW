print("READING AND WRITING FILES IN PYTHON")
#list of commands to read and write files in python language
#close - closes the file
#read - reads the content of the files
#readline -- reads the content of the line and not the whole thing or content
#truncate -- deletes or empties the file
#write -- wwrites the stuff to a file
#lets make a simple text editor
from sys import argv
script, filename = argv
print("we're going to erase %r"% filename)
print(" if you want an interruption you can press or hit the keys CTRL+^C")
print("If you want that then hit RETURN")

input("what do you want?")
print("opening the file..")
target = open(filename, 'w')

print("truncating the file, goodbye!")
target.truncate()

print("now we're going to wrte three lines to the file step by step")
line1 = input("enter the line")
line2 = input("enter the line")
line3 = input("enter the line")
print("I'm going write these lines to the file now..")
#lines= (line1,line2,line3)
line = '{}\n{}\n{}\n'.format(line1,line2,line3)
target.write(line)
#target.write("%s\n%s\n%s\n" %(line1,line2,line3))
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
print("and we finally close it")
target.close()
# theres another way to do this and that is via formatting
#target.write'{}\n{}\n{}\n'.format(line1,line2,line3)
#target.write(line)
# we can do this too.. target.write('\n'.join((line1, line2, line3))+'\n')