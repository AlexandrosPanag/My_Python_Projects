import re


with open(r'C:\Users\ASL_7\Desktop\rexample.txt', encoding='utf-8') as f: #open the file to the specific location

    findvowels=f.read()
#find vowel letters on a txt
    print("\nWords that contain vowels:")
    vowels = r"\b[aeiou][\w]*" #notice that y sometimes acts as a consonant and sometimes it acts as a vowel if we want, we can add y
    print(re.findall(vowels,findvowels,re.I)) #find words that contain vowels
f.close