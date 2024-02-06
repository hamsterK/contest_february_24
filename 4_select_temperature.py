"""
Task: Select Temperature
There's an air conditioner in the office.
First, input the number of rounds.
Then, input the number of people in the room.
After that, indicate each person's desired temperate in the format '>= X' or '<= X'.

After each temperature input, a temperature satisfying everyone in the room is displayed.
If agreement cannot be reached at this moment, the expected output is '-1'.
"""

for i in range(int(input())):
    temperatures = []
    for j in range(int(input())):
        sign, desired_temp = input().split()
        if sign == '>=':
            temperatures.append(set(range(int(desired_temp), 31)))
        else:
            temperatures.append(set((range(15, int(desired_temp) + 1))))
        try:
            print(list(set.intersection(*temperatures))[0])
        except IndexError:
            print('-1')
    print()

"""
Test input:
4
1
>= 30
6
>= 18
<= 23
>= 20
<= 27
<= 21
>= 28
3
<= 25
>= 20
>= 25
3
<= 15
>= 30
<= 24

Test output:
30

18
18
20
20
20
-1

15
20
25

15
-1
-1
"""