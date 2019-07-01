print("EXERCISE 21:functions that returns something")
def add(a,b):
    print("adding %d + %d" % (a,b))
    return(a+b)

def subtract(a,b):
    print("subtracting %d - %d " % (a,b))
    return(a-b)

def multiply(a,b):
    print("multiplying %d*%d" %(a,b))
    return(a*b)

def divide(a,b):
    print("dividing the two nos %r/%r" %(a,b))
    return(a/b)

print("lets do some math with functions ")
age = add(30,5)
height= multiply(6,19)
weight = subtract(100,30)
iq = divide(200,2)

print(""" the age is %r,
the height is %r,
the weight is %r and
the iq is given as%r""" %( age, height, weight, iq))

print("here's a puzzle")
what = add(age,subtract(height,multiply(weight, divide(iq,2))))
print ("that becomes", what, "cab you do it by hand?????")
