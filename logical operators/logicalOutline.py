'''
This outline will help solidify concepts from the Logical Operators lesson.
Fill in this outline as the instructor goes through the lesson.

boolean/comparison + logical operator + boolean/comparison

simplifies to another boolean 

and
or 
not logical operator + boolean
'''

#EX) Make two boolean variables. Put them on either side of the and operator.
#Store this expression in a variable named a. Print the variable.
one = True
two = False
a = one and two 
print(a)

#1) Make two boolean variables. Put them on either side of the and operator.
#Store this expression in a variable named a. Print the variable.

three = True 
four = False

a = three and four 
print (a)


five = True 
six = True

a = five and six 
print (a)


seven = False
eight = False

a = seven and eight 
print (a)

#2) Make two boolean variables. Put them on either side of the or operator.
#Store this expression in a variable named b. Print the variable.

one = True
two = False

b = one or two 
print (b)


three = True
four = True 

b = three or four 
print (b)


five = False 
six = False 

b = five or six 
print (b)

#3) Make one boolean variable. Put the variable after the not. Store this 
#expression in a variable named c. Print the variable.

c = not 3==3 
print (c)

c = not 4 == 5 
print (c)

#4) Make a logical expression with one of the common SYNTAX errors.
z = 4 < 3 or 5 < 10 
print (z)
 
''' 
The common mistake here is just forgetting the comparison on 
the other side of the "or". There is also missing operator or comparison data
'''
