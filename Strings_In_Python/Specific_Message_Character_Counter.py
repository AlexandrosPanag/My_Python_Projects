letter_counter = {} #creating a counter to count each letter

text = input("Give a message to count the length :")

for i in text: 
    letter_counter[i] = letter_counter.get(i,0) + 1

for i in sorted(letter_counter.keys()):
    print( i , " : ", letter_counter[i])