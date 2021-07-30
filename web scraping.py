import urllib, re
import urllib. request
sites=['http://google.com','http://rediff.com']
for site in sites:
    print(f'searching.... for..{site} ')
    u=urllib. request. urlopen(site)
    text=u. read()
    title=re. findall('<title>.*</title>',str(text),re. IGNORECASE)
    print(title[0])