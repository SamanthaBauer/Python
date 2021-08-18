'''
This outline will help solidify concepts from the Conditionals lesson.
Fill in this outline as the instructor goes through the lesson.

if/elif/else + (conditional statement): 
    code block
    
    CODE BLOCKS ARE TABBED IN!!!!!
'''

#1) Make a int variable named a. Now make an if statement, and if a is more than
#5, print out "a is more than 5."

a = 7 
if (a > 5):
    print ("The a value is more than 5.")

#2) Make a boolean variable named b. Now make an if statement, and if b is True
#print out "b is True."

b = True 
if (b == True): 
    print ("b is True")

#3) Make an int variable named c. Now make an if/elif statement, and if c is 
#more than 0, print "c is positive". Else if c is less than 0, print "c is
#negative".

c = -5
if (c >= 0): 
    print ("The c value is positive.")
else: 
    print ("The c value is negative.")

#4) Make an int variable named d. Now make an if/elif/else statement, and if 
#d is more than 0, print "d is positive". Else if d is less than 0, print "c is
#negative". Else, print "d is zero".

d = 13 
if (d < 0):
    print ("The d value is negative.")
elif (d == 0):
    print ("The d value is zero.")
else: 
    print ("The d value is positive.")

#5) Make an if statement with any comparison, with a common SYNTAX error.

''' A common syntax error is forgetting the parentheses after the if or elif.
Another one is forgetting to put the colon after the print function. Also 
misspelling if/elif/else. Also not having the code block tabbed in is also
another syntax error. Also putting the different conditions out of order can
read you an error message. Having a comparison that is wrong.''' 
    
    
password = "mjw11343"

if (password == "adsfhg"): 
    print ("You got the password!")
else: 
    print ("Wrong password. Try again.")
    


