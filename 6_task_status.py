"""
Task: Check that the task status are correct
First number of tasks in input.
Then on each line the list of status is provided as str.
Yes receives the answer whether the flow for the task was correct.

Final status should always be 'D'.

List of status with the statuses it can be converted to:
M - Main - R, C, D
R - Reopened - C
C - Cancelled - M
D - Done - M
"""
import sys


def fast_input():
    return sys.stdin.readline().rstrip("\r\n")


def fast_output(x):
    sys.stdout.write(str(x + '\n'))


def check_flow(status_1, status_2):
    if status_1 == 'B':
        return status_2 == 'M'
    elif status_1 == 'M':
        return status_2 in 'CRD'
    elif status_1 == 'R':
        return status_2 == 'C'
    elif status_1 == 'C' or 'D':
        return status_2 == 'M'


for i in range(int(input())):
    flow = fast_input()
    if flow[-1] != 'D':
        fast_output('NO')
        continue
    result = 'YES'
    status_1 = 'B'
    for j in range(len(flow)):
        status_2 = flow[j]
        if check_flow(status_1, status_2) is True:
            status_1 = status_2
        else:
            result = 'NO'
            break
    fast_output(result)

"""
Test input:
5
MRCMD
MDD
M
MDMRCMD
MMDD

Test output:
YES
NO
NO
YES
NO
"""