'''
This is an exercise drill that you can try if you want to practice making
more Comparison operations.
'''


#1) Make a boolean variable. Make an if statement. If the boolean is true
#print "Boolean is True".

boolean = True
if (boolean):
    print ("boolean is true")

#2) Make two string variables: a, and b. Make an if statement. If a is 
#equal to b, then print "a equals b."

a = "Samantha"
b = "samantha"
if (a ==b):
    print ("a equals b.")
else: 
    print ("a does not equal b")

#3) Make two int variables: c, and d. Make an if statement. If c is equal
#to d, then print "c equals d.".

c = 1 
d = 2 

if (c == d ): 
    print ("c equals d")
else: 
    print ("c does not equal d")

#4)Make three boolean variables. Make an if/elif statement. If all the
#booleans are true, print "All true". Elif any (but not all) are true, 
#print "Some are true".

e =True 
f = True 
g = True 

if (e and f and g):
    print ("all true")
elif (e or g or f):
    print ("some are true")
else: 
    print ("neither")

#5)Make a string that one of these characters: a, b, or c. Make an if/elif
#statement. If the string equals a, print "A is incorrect". elif the string
#equals b, print "B is incorrect". Elif the string equals c, print
#"C is correct".

string = "c"
if (string == "a"): 
    print ("a is incorrect")
elif (string == "b"):
    print ("b is incorrect")
elif (string == "c"):
    print ("c is correct")
