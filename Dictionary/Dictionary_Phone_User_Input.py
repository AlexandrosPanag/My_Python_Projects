# By Alexandros Panagiotakopoulos - alexandrospanag.github.io

# Creating a dictionary
myDictionary = {6888888888: 'Arthur', 6777777777: 'Merlin', 699999999: 'Lancelot'}

# enter the key for which the value to be obtained
print("Enter the phone number to find the user")
givenkey= int(input())

# Traversing the keys of the dictionary
for i in myDictionary.keys():

   # checking whether the value of the iterator is equal to the above-entered key
   if(i==givenkey):

      # printing the value of the key
      print(myDictionary[i])