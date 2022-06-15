myfile = 'myfile.txt'

try:
    with open(myfile,'r',encoding = 'utf-8') as f:
        works = f.read()
    for line in works.split('\n'):
        print(line)
except IOError as e:
    print(e)
    