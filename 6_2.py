'''
Complete soltion of Book 
"Python For Software Design by Allen B. Downey"
by Harsh Bhatia ( www.harshbhatia.net )
'''
'''Exercise 6.2
Use incremental development to write a function called hypotenuse that returns
the length of the hypotenuse of a right triangle given the lengths of the two legs as
arguments. Record each stage of the development process as you go'''
import math
def hypotenuse(x,y):
  x=x*x
  # print x
  y=y*y
  print math.sqrt(x+y)

hypotenuse(3,4)
