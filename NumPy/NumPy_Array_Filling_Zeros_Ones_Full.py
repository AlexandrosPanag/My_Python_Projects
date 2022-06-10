import numpy as np #importing numpy you might need to run the command <pip install numpy>, in case it is not
#recognized by visual studio code , set the numpy name to np

myzeroarray=np.zeros(5) #creating a 5-row zero array
print("\nMy zero array: \n")
print(myzeroarray) #outputting the array

myonearray=np.ones((2,3), dtype = int) #creating a two dimensional 2 row x3 column array full of 1s in integer format
print("\nMy one array: \n")
print(myonearray) #outputting the array

myfullarray=np.full((3,5),8) #creating a 3x5 array full of 8
print("\nMy full array: \n")
print(myfullarray)