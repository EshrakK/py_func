# Regex for BD phone numbers

import re

phn_num = '''
+880 1011-705197
01053-055031
010-434-13498
+880 1019-090440
'''

pattern = re.compile(r'[+]?(88)?0\s?(\d{4}|\d{2})?-*(\d{6}|\d{3})?-(\d{5})?')
matches = pattern.finditer(phn_num)
for match in matches:
    print(match)
