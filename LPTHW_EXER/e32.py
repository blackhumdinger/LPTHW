print("exercise 32 loops and list")
hair = ['brown', 'black','blonde','red']
eyes = ['brown', 'blue', 'black']
weights = [39,67,86,44]
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print("the count is %r" %number)

for fruit in fruits:
    print("the name of fruits is %s" % fruit)

for i in change:
    print("the change value is %r" % i)

elements = []
for i in range(0,6):
    print("adding %d to the list" %i)
    elements.append(i)

for i in elements:
    print(" the element is %d" %i)

#FACTS
# for loop initializes variables everytime it is given the command to do so
