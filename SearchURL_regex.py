# Regex for searching urls

import re

urls = '''
https://www.google.com
http://alphabet.com
https://youtube.com
https://www.nasa.gov
'''
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(0))    #prints out all the urls
    #print(match.group(1))   #prints only the 'www' part of url
    #print(match.group(2))   #prints only the text in between '.'
    #print(match.group(3))   #prints only the '.com'
    