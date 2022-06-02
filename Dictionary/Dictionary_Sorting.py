dd = {1:20, 5:10, 3:15} #creating a dictionary

print("\nOnly the dictionary keys are printed: \n")
for i in dd: #printing only the keys of the dictionary
    print(i)

print("\nThe dictionary keys and the elements are printed: \n")
for i in dd:
    print(i,'->',dd[i]) #printing the key and where the dictionary is showing

print("\nSorted order by dictionary key order: \n")
for i in sorted(dd): 
    print(i,'->',dd[i]) #printing the key sorted by the key value in order

print("\nSorted order by dictionary element order: \n")
for i in sorted(dd,key = dd.get):
    print(i,'->',dd[i]) #printing the dictionary elements sorted by the value in order