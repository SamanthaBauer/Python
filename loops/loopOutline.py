'''
This outline will help solidify concepts from the Variables lesson.
Fill in this outline as the instructor goes through the lesson.

while a condition is true, a block of code will repeat

while (condition):
    code block
    
for [item] in [iterable]: 
    code block
    
iterable means to repeat (variables that can be repeated) such as lists or 
strings. 

'''

#1) Make a int variable called x set to 0. Make a while loop that prints 
#out x and increments it by one. Make the loop run while x is less than
#or equal to 20.

x = 0 

while (x <= 20):
    print (x)
    x = x + 1 
    
#2) Make a int variable called x set to 0. Make a while loop that prints 
#out x and increments it by one. Add an if statement that breaks the loop
#if x equals 15. Make the loop run while x is less than 100.

x = 0 
while (x < 100):
    print (x) 
    x = x + 1 
    if (x == 15):
        break


#3) Make a int list with three items inside. Make a for loop that prints 
#out all the items.

var = [1, 2 ,3]
for x in var: 
    print (x)

#4) Make a string list with three items inside: "Michael", "Chris", "Nino". 
#Make a for loop that prints out all the items. Add an if statement that 
#breaks the loop if the item equals "Chris".

var = ["Michael", "Chris", "Nino"]

for x in var:
    print (x)
    if (x == "Chris"):
        break

#5) Make a while loop with a common SYNTAX error.

''' miss typing the while. having the incorrect condition. missing the 
colon after the condition. not indenting print.    '''

#6) Make a for loop with a common SYNTAX error.

''' miss typing the for or the in, not having the item or the iterable. 
missing the colon or the code block. not indenting print  '''
