# Write a program to print a Hollow Pyramid of N rows using stars (*), where integers
# N is given as an input

'''
first_row = (n - 1) * (" ") + ("* ")
n spaces stars
6   5      1
4   3      1

   n - 1

last_row 
n * "* "

n = 6
middle_row 
  initial "* " hollow "* "
i spaces stars spaces stars
2   4      1     0      1
3   3      1     2      1
4   2      1     4      1
5   1      1     6      1
   n-i     1  2*i - 4   1

i + initial_spaces = n
initial_spaces = n - i
hollow_spaces = 2 * i - 4
'''

n = int(input())
for i in range(1, n+1):
    if i == 1:
        spaces = (n - 1)
        row = spaces * " " + "* "
    elif i == n:
        row = n * "* "
    else:
        initial_spaces = (n - i)
        hollow_spaces = 2 * i - 4
        row = initial_spaces * " " + "* " + hollow_spaces * " " + "* "
    print(row)