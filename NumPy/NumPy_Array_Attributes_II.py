import numpy as np #importing numpy you might need to run the command <pip install numpy>, in case it is not
#recognized by visual studio code , set the numpy name to np

integers = np.array([[1, 2, 3],[4 ,5 ,6]]) #in some platforms it will output int64, the output in this case was int32
 
floats = np.array([0.0, 0.1, 0.2, 0.3, 0.4]) #the output will be float 64

print(integers.size) #printing the size of the integers array if the output of np.array is int32, like in my case you use this command
#otherwise you might be required to use integers.itemsize
print(floats.size) #printing the size of the floats array

print("\n Printing the Integer array elements:")
for row in integers:
    for column in row:
        print(column, end=' ')
    print()

print("\n Printing the intger array elements like they were on a one-dimensional array:")
for i in integers.flat:
    print(i,end=' ')