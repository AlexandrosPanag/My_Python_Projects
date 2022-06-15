import re

# example user inputs : h1,h2,h3 etc
with open(r'C:\Users\<Users>\Desktop\ALEX_GITHUB.html', encoding = 'utf-8') as f:
    html = f.read()

#print(html)

email_pattern = r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'


while True:
    tag = input('Give an html label:')
    if tag == '': break
    tag_pattern = r'<'+tag+r'\b[^>]*>(.*?)</'+tag+r'>'
    found = re.findall(tag_pattern, html, re.I)
    found = list(set(found))
    for f in found :print('\t\t', f)