import urllib.request
import urllib.error

# do not forget to remove the < > where you paste the website & the html file
url = urllib.request.Request('<https://www.websiteexample.com>')

try:
    with urllib.request.urlopen(url) as response:
        char_set = response.headers.get_content_charset()
        html = response.read().decode(char_set)
    with open("<website.html>","w",encoding = char_set) as p:
        p.write(html)
except urllib.error.HTTPError as e:
    print(e.code)
    print("HTTP Error")
except urllib.error.URLError as e:
    if hasattr(e,'reason'):
        print("Failed to connect to the server")
        print("Reason:",e.reason)
else:
    print("End of program")