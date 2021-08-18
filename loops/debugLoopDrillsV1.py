'''
The following functions have problems that keep them from
completing the task that they have to do.

All the problems are either Logical or Syntactical errors with LOOPS.
Focus on the loops and find the problems with the LOOPS.

The number of errors are as follows:
counting: 4
fruits: 3
checkStudents: 3
printGrades: 2
'''

'''
This function uses a while loop to print out every number from
1 to 100.
'''
def counting():
    x = 0
    y = 100
    while (x <= y):
        x = x + 1
        print (x)
    return

counting()

'''
This function takes a list of fruits and prints out each fruit in the list using
a for loop.
'''
def fruits(fruit):
    for fruits  in fruit:
        print(fruits)
    
    
listOFruit = ["apple", "pear", "peach", "watermelon", "tomato"]
fruits(listOFruit)


'''
This function takes a list of grades and then prints each of the grades out with
a for loop.
'''
def printGrades(studentList):
    for grade in studentList:
        print(grade)
    print("DONE")
    return 

listOfStudents = [66, 24, 12, 45, 100, 100, 100]
printGrades(listOfStudents)
        