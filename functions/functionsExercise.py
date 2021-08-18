'''
This is an exercise drill that you can try if you want to practice making
more functions.
'''

#1) Make a function that has one parameter: list. Make the function print out 
#each item in the list. It shouldn't return anything. Then, call the function.
#Print what the function returns.

def happyOne(flowerOne):
    for x in flowerOne:
        print(x)
        return 
    
flowerOne = [1, 2, 3, 4, 5, 6]
print (happyOne(flowerOne))

#2) Make a function that has one int parameter: radius. Make the function
#calculate the circumference of a circle using radius (the calc is: 2 * radius
# * 3.14). Then return the circumference. Then call the function.
#Print what the function returns.

def circum(radius):
    circum  = 2 * radius * 3.14
    return circum

print (circum(4))

#3) Make a function that has two int parameters: l and w. Make the funciton
#calculate the area of a rectangle using l (length) and w (width) (the calc
#is l * w). Then return the area. Then call the function.
#Print what the function returns.

def area (l, w):
    area = l * w
    return area 

print (area(3, 4))

#4) Make a function that has one parameter: list. Make sure it is a string list.
#Make the function combine each string in the list into one string, using 
#a for loop. Then return the combined string. Then, call the function.
#Print what the function returns.

def happy(flower):
    combine = " "
    for x in flower:
        combine = combine + x 
    return combine

flower = ["Michael", "Juan", "AJ", "Nino"]
print(happy(flower))
