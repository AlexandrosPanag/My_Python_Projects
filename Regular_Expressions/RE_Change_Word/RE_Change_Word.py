import re


with open(r'C:\Users\ASL_7\Desktop\rexample.txt', encoding='utf-8') as f: #open the file to the specific location

    regular=f.read()
#changing the regular word
    print(re.sub(r'\bregular\b','REGULAR',regular)) #change the regular word to REGULAR

f.close