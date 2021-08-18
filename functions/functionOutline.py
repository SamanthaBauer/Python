'''
This outline will help solidify concepts from the Functions lesson.
Fill in this outline as the instructor goes through the lesson.
'''
'''
def [nameOfFunction] (parameter):
    code block
    return [variable/data]
    
always has start with letter
camel casing, but short as possible (can have number, but not preferred)
no key words (name them in a way that python allows it)

'''
def sumTwoNums(numOne, numTwo):
    number = numOne + numTwo
    return number
x = 2 
y = 3 
num = sumTwoNums(x, y)

print (num)


def happy(flower):
    for x in flower: 
        print (x)
    return

a  = ("string", "string", "string")
happy(a)

b = ("True", "False", "True","False")
happy(b)

#1) Make a function that has two boolean parameters. If both booleans are
#true, return true. Else, return false. Then, call the function.
#Print what the function returns.

def answer (y, z):
    if y == True and z == True: 
        return True 
    else: 
        return False
    
print (answer (True, False))   


#2) Make a function that takes one int parameter: gallons. Convert gallons
#to cups (do this by multiplying gallons by 16). Then return cups. Then,
#call the function.
#Print what the function returns.

def number(x):
        cups = x * 16
        return cups 

x = 44

cups = number(x)

print (cups)

#3) Make a function of any any kind with a common SYNTAX error. Then, call the
#function.
#Print what the function returns.

''' A common syntax error would be forgetting the colon after the parameter. 
Another common syntax error would be not returning the function once you called
it. Otherwise another one would be trying to call a funtion when there is 
nothing to call.'''
