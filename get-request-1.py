from urllib.request import urlopen
html = urlopen("http://www.google.com/").read()
print(html)