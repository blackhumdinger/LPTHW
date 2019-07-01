print("EXERCISE 24: more practice")


print("lets practice everything")
peom = """
\tEvery blasted acrimonious misdeed
aye indelibly perpetrated
affecting ye\n and the Punim for life
hounds me doggone soul night and day
venomous wrath torments, strangles, racks...
\n\tevery bone in mine entire body




"""

five = 10-2+3-6
print("this should be five %s" % five)

def secret_formula(started):
    jelly_beans = started*500
    jars = jelly_beans/10
    crates = jars/100
    return jelly_beans, jars,crates


start_point= 100
beans, jars, crates = secret_formula(start_point)
print("with a start piont of %r we'd have %r beans, %r jars and %r crates" %(start_point, beans,jars,crates))
start_point = start_point/10

print("we can also do it this way")
print("we'd have%d beans, %d jars, and %d crates" % secret_formula(start_point))
