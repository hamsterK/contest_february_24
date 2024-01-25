"""
Task: Date validate
Check if the date provided exists
"""

from datetime import datetime
for i in range(int(input())):
    day, month, year = [int(j) for j in input().split()]
    try:
        datetime(day=day, month=month, year=year)
        print('YES')
    except ValueError:
        print('NO')

"""
test input:
10
10 9 2022
21 9 2022
29 2 2022
31 2 2022
29 2 2000
29 2 2100
31 11 1999
31 12 1999
29 2 2024
29 2 2023

test output:
YES
YES
NO
NO
YES
NO
NO
YES
YES
NO
"""