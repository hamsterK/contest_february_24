"""
Task: output difference between actual income and expected income
Incorrect % of interest was calculated initially (rounded to whole number).
Output the lost profit.

First, input the number of rounds.
Then, input the number of sold items and expected % if interest.
After that, input the price of sold items each on new line.

After each set, lost profit is displayed.
"""


import sys


def fast_input():
    return sys.stdin.readline().rstrip("\r\n")


def fast_output(x):
    if len(str(x).split('.')[1]) == 1:
        sys.stdout.write(str(x) + '0')
    else:
        sys.stdout.write(str(x))


for i in range(int(input())):
    quantity, percentage = map(float, fast_input().split())
    lost_money = float()
    for j in range(int(quantity)):
        price = float(fast_input()) * percentage * 0.01
        lost_money += round(price, 2) - int(price)
    fast_output(round(lost_money, 2))
    print()

"""
Test input:
3
5 1
1
2
3
4
5
1 5
40
2 99
50
1

Test output:
0.15
0.00
1.49
"""