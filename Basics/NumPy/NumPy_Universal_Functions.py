import numpy as np

numbers = np.array([1,4,9,12,15,18])
numbers2 = np.arange(1,7)*10
addednumberarray=np.add(numbers,numbers2) #adding the two arrays (each element with each element)
mulnumberarray=np.multiply(numbers,numbers2) #multiplying the two arrays

print("The added array is:",addednumberarray)
print("The multiplied array is:",mulnumberarray)

#side note:
# a few other commands can be:
# Maths: subtract,multiply,divide,remainer,exp,log,sqrt,power etc
# Trigonometry: sin,cos,tan,hypot,arcsin,arccos,arctan etc
# Comparison: greater, greater_equal, kess, less_equal, equal, not_equal, logical_and,logical_or, logical_xor,logical_not,minimum, maximum etc.
# Floating Point Numbers: floor, ceil, isinf,isnan,fabs,trunc
