'''
i j(max)
0 0
1 1
2 2
3 3

i = 0 -- n - 1
j = 0 -- i + 1

i = 0, j = 0
i = 1, j = 0, 1
i = 2, j = 0, 1, 2
'''

n = int(input())
for i in range(n):
    for j in range(i+1):
        print("* ", end="")
    print()