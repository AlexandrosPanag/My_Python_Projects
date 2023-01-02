# By Alexandros Panagiotakopoulos - alexandrospanag.github.io

#quadratic equation ax^2+bx+c =0
#asking from the user a, b ,c inputs

a=input("Give the value of a= ") #taking a as an input
b=input("Give the value of b= ") #taking b as an input
c=input("Give the value of c= ") #taking c as an input
print("The values will be solved:\n") #print the solution
print("{}x**2 + {}x  + {} = 0".format(a,b,c)) #print the formula
a = float(a)
b = float(b)
c = float(c)

if a == 0 :
    if b == 0:
        if c == 0 :
            print("There are infinite sulutions")
        else :
            print("There are no solutions")
    else:
        print("The values are x1 = x2 = {:1.2f}".format(-c/b))

qe= b**2 - 4 *a * c #qe stands for quadratic equation we use the formula
print("The discriminant is {:1.2f}".format(qe)) #printing the discriminant

if qe < 0: #if the quadratic equation is below zero then 
    print("The equation is only having complex numbers as a solution") #print tat the equation is only having complex numbers as a solution
else : #the quadratic equation can be solved
        x1 = (-b+qe**0.5)/(2*a)
        x2 = (-b-qe**0.5)/(2*a)
        print("The solutions are:x1 = {1.2f}, x , x2 = {1.2f} ".format(x1,x2))
