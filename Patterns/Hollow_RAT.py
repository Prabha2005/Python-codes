# Write a program to print a hollow right angle triangle of N rows using stars (*), 
# integer N is given as an input.

'''

n = 6

first = spaces, stars
middle = spaces, stars, spaces, stars
last = stars

first_row -- spaces = 2 * (n - 1)
n spaces spaces % 2 stars
6   10         5      1
5   8          4      1
           n - 1

last_row -- stars = n

middle_row

i initial_spaces initial_spaces % 2 stars hollow_spaces stars
2    8                  4             1         0         1
3    6                  3             1         2         1
4    4                  2             1         4         1
5    2                  1             1         6         1
           (n - i) * 2                1                   1

initial_spaces % 2 + i = n
initial_spaces = (n - i) * 2

hollow_spaces = 2 * i - 4

first_row = spaces * " " + ("* ")
middle_row = initial_spaces * (" ") +  .... ("* ") + hollow_spaces * (" ") + ("* ")
last_row = stars * "* "

'''
n = int(input())
for i in range(1, n+1):
    if i == 1:
        spaces = 2 * (n - 1)
        row = spaces * " " + "* "
    elif i == n:
        row = n * "* "
    else:
        initial_spaces = 2 * (n - i)
        hollow_spaces = 2 * i - 4
        spaces = 2 * (n - 2)
        row = initial_spaces * " " + "* " + hollow_spaces * " " + "* "
    print(row)