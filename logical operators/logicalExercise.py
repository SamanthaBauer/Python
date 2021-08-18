'''
This is an exercise drill that you can try if you want to practice making
more logical operations.
'''

#1) Make four string variables named a, b, c, and d. Make a new variable e and
#compare a to b and c to d, using the == operator. Make it so if both
#comparisons are true, e will be true. Then print e.

a = "one"
b = "two"
c = "three"
d = "three"

e = a == b or c ==d 
print (e)

#2)Make four int variables named f, g, h, and i. Make a new variable j and 
#compare f to g and h to i, using the > operator. Make it so if both comparisons
#are true, then j will be true. Then print j.

f = 1 
g = 2 
h = 3 
i = 4 

j = f > g and h > i 
print (j)

#3)Make four boolean variables named k, m, n, o. Make a new variable p and
#compare k to m and n to o, using the == operator. Make it so if either
#comparisons are true, then p will be true. Then print p.

k = True
m = False
n = True
o = True

p = k == m or n == o 
print (p)


#4) Make two boolean variables named q and r. Make a new variable s and
#compare q to r, using the == operators. Make it so if the comparison is True,
#then s will be False (and if the comparison is False, then s will be True). 
#Then print s.

q = True
r = True

s = not q == r 
print (s)
