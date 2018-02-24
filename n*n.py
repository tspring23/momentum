#! /usr/bin/python

import sys
import time
import random
from sympy import *

def ipop():
  while True:
    str1 = raw_input("Enter a number to make n*n matrix :")
    #a = type(str1)
    #print a
    print "we will make" , str1,"*",str1,  "matrix A and do some calculations" 
    
    if str1.isdigit() == True:
       n = int(str1)
       break

    else: 
       print "But,", str1, "is not a number"
       continue

  return n


before = time.clock()

#str = raw_input("please enter a number: ")
n = ipop()
 
j = 1
Z =[]

while j <= n*n:
      Z.append(Rational(1,random.randint(1,10))) 
      j = j +1

B = Matrix([Z])
A = B.reshape(n,n)


print "A is  ", A
E = eye(n)

print "E-A is ", E-A
print "E-A.inv() is  ", (E-A).inv()
print "(E-A)*((E-A).inv()) is E = ",(E-A)*((E-A).inv())


print "Time is... ", (time.clock()-before)
