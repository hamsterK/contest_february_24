"""
Task: License plates
Check if the line contains of valid license plates
"""

import re

plate_format = r'([A-Za-z]\d{1,2}[A-Za-z]{2})'

for i in range(int(input())):
    string = input()
    groups = re.findall(plate_format, string)
    if len(string) != sum([len(plate) for plate in groups]):
        print('-')
    else:
        print(*groups, sep=' ')

"""
Test input:
6
R48FAO00OOO0OOA99OKA99OK
R48FAO00OOO0OOA99OKA99O
A9PQ
A9PQA
A99AAA99AAA99AAA99AA
AP9QA

Test output:
R48FA O00OO O0OO A99OK A99OK
-
A9PQ
-
A99AA A99AA A99AA A99AA
-
"""
