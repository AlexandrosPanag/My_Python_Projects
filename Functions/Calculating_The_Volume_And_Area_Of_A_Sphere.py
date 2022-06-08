# e = 4*pi*r**2
# v = (4/3)*pi*r**3

import math

pi = math.pi

def area(r):
    return 4*pi*r**2

def vol(r):
    return (4/3)*pi*r**3
def isnum(n):
# function that checks if a string is a number
    if not type(n) is str:
        return False
    n= n.strip()
    if n.isdigit():
        return True   
    elif n[0] in '+-' and isnum(n[1:]):
        return True
    elif "." in n:
        if n.count(".")==1 and isnum(n.replace(".","")):
          return True
        else:
            return False
    else:
        return False

while True:
    r = input("Give Radius or write <stop> to stop the program : ")
    if r == 'stop':break
    if isnum(r):
        v=vol(float(r))
        e=area(float(r))
        print("Area={:1.2f}, volume={:1.2f}".format(e,v))
    else:
        continue