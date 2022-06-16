import urllib.request
import urllib.error
import re
url_dept = '6' #the website that we want , one possible example is 'https://service.eudoxus.gr/public/departments/courses/3008/2016'

try:
    req = urllib.request.Request(url_dept)
    with urllib.request.urlopen(req) as response:
        char_set = response.headers.get_content_charset()
        html = response.read().decode(char_set)
except urllib.error.HTTPError as e:
    print('HTTP Error:', e.code)
except urllib.error.URLError as e:
        print('Failed to connect to the server')
        print('Reason: ', e.reason)
else:
    h2_tags = re.findall(r"<h2\b[^>]*>(.*?)</h2>", html)
    count = 0
    for tag in h2_tags:
        code = re.findall(r"\[(.*?)\]", tag)
        if len(code)> 0 :
            code = code[0].strip()
            name = re.findall(r']:(.*)', tag)
            if len(name) > 0 : name = name[0].strip()
            else: name = ''
            print(code, name)
            count += 1
    print('Retrieved {} website registries '.format(count))