letter_counter = {} #creating a counter to count each letter

text = input("Give a message to count the length :")

for i in text: 
    #if i.isalpha(): optional command if we want to skip the null to be counted
    letter_counter[i] = letter_counter.get(i,0) + 1

for i in sorted(letter_counter.keys()):
    print( i , " : ", letter_counter[i])
