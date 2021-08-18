'''
This is an exercise drill that you can try if you want to practice making
more Comparison operations.
'''

#1) Make a boolean variable set to True. Make a while loop that prints 
#out the boolean variable. Make the while loop run while your boolean
#is True. Add an if statement that breaks the loop if your boolean is True.

boolean = True
while (boolean): 
    print(boolean)
    if (boolean):
        break

#2) Make a int list named ints with 3 items. Make an int named x set to
#zero. Make a while loop that runs while x is less than the length of
#ints. (You can calculate the length of lists with: len(nameOfList).
#In the loop, print out each item in the list. (Use x for the index:
#nameOfList[x]).  Then, increment x by one.

x = 0 
ints = [1, 2, 3]
while ( x < len (ints)): 
    print (ints[x])
    x = x + 1 

#3) Make a int list with 3 items. Make a for loop that prints out all the
#items.

number = [1,2,3]
for x in number: 
    print (x)

#4) Make a int variable called x set to 0. Make a while loop that prints 
#out x and increments it by one. Add an if statement that breaks the loop
#if x equals 5. Make the loop run while x is less than 10.

x = 0 
while (x < 10): 
    print (x)
    if (x == 5): 
        break
