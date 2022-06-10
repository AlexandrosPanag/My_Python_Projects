import numpy as np #importing numpy you might need to run the command <pip install numpy>, in case it is not
#recognized by visual studio code , set the numpy name to np

integers = np.array([[1, 2, 3],[4 ,5 ,6]]) #declaring an integer array
 
floats = np.array([0.0, 0.1, 0.2, 0.3, 0.4]) #declaring a float array

print(integers.dtype) #in some platforms it will output int64, the output in this case was int32
print(floats.dtype) #the output will be float 64
