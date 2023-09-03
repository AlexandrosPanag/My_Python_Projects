import re

try:
    with open(r'C:\Users\<Username>\Desktop\1984.txt', encoding='utf-8')as f:
        works = f.read()
    for line in works.split('\n'):
        print(line)
except IOError as e:
    print(e)
while True:
    keyword = input("Give a keyword:")
    if keyword == '':break
    n_phrase=''
    for c in keyword:
        char = c
        n_phrase += char
    print(n_phrase)
    pattern = ".*"+n_phrase+".*"
    w = re.findall(pattern,works,re.I)
    for work in w:
        print(work)