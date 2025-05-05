import numpy as np #importing numpy you might need to run the command <pip install numpy>, in case it is not
#recognized by visual studio code , set the numpy name to np

numbers = np.arange(1,6)
numbers2 = np.linspace(1.1, 5.5, 5) #make an array of elements from 1.1 to 5.5 for 5 elements
print("\nThe first list contains:\n",numbers) #print the first array of elements
print("\nThe second list contains:\n",numbers2) #print the second array of elements

print("\n",numbers>3) #print from the first array the numbers that are above 3
print("\n",numbers2> 3.3) #print from the second array the list of elements that are above 3.3
 

# A few examples with logical operations/ comparison between the two arrays
print("\n",numbers*numbers2)
print("\n",numbers2<numbers)
print("\n",numbers == numbers2)
