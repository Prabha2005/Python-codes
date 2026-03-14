# Write a program to print a pyramid of N rows using stars (*), where integer N is given as an input

'''
i  spaces no_of_spaces  stars(no_of_stars - 1) no_of_stars(2i)
1    6                    1                         2
2    4                    3                         4
3    2                    5                         6
4    0                    7                         8

no_of_spaces % 2 + i = n
no_of_spaces % 2 = (n - i)
no_of_spaces = 2(n - i)

stars = 2i - 1
'''

n = int(input())
for i in range(1, n+1):
    spaces = 2 * (n - i)
    stars = (2 * i) - 1
    rows = spaces * " " + stars * "* "
    print(rows)