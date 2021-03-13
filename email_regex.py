# Regex for email address


import re
emails = '''
timothy145@gmail.com
geofry.hinton@university.edu
max-321-payne@my-work.net
'''
pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|net|edu)')
matches = pattern.finditer(emails)
for match in matches:
    print(match)
    