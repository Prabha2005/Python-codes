# Write a program to print a Hollow Pyramid of N rows using numbers starting from 5, where
# integer N is given as an input

''' 
first_row = spaces, numbers -- (n - 1)


middle_row = spaces, number, mid_spaces, final_num -- 
i spaces numbers mid_spaces final_num
2   4       5       0           6
3   3       5       2           7
4   2       5       4           8
5   1       5       6           9
   n - i    5    2*i - 4      i + 4

spaces + i = n
spaces = n - i

spaces = 2 * i + c
   2   = 2 * 3 + c
   2   = 6 + c
   -c  = 6 - 2
   c   = -4

final_num = i + c
    7     = 3 + c
    c     = 7 - 3
    c     = 4   

last_row = numbers -- print(j + 4, end = " ")

n spaces
4   3
6   5

i = n
j = 1 to N
'''

n = int(input())
for i in range(1, n+1):
    if i == 1: # first_row
        spaces = (n - 1) * " "
        row = spaces + str(5) + " "
        print(row)
    elif i == n: # last_row
        for j in range(1, n+1):
            print(j + 4, end = " ")
    else: # middle_row
        spaces = (n - i) * " "
        mid_spaces = (2 * i - 4) * " "
        row = spaces + str(5) + " " + mid_spaces + str(i + 4) + " "
        print(row)

