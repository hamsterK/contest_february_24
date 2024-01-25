"""
Task: Battle ship game
Verify that the list of ships is correct for the game
"""

ships = ['1', '1', '1', '1', '2', '2', '2', '3', '3', '4']
for i in range(int(input())):
    print('YES') if ships == sorted(input().split()) else print('NO')

"""
test input:
5
2 1 3 1 2 3 1 1 4 2
1 1 1 2 2 2 3 3 3 4
1 1 1 1 2 2 2 3 3 4
4 3 3 2 2 2 1 1 1 1
4 4 4 4 4 4 4 4 4 4

test output:
YES
NO
YES
YES
NO
"""