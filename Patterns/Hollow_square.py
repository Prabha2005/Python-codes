# Write a program to print a Hollow Square of N rows and N columns using stars (*), where
# integer N is given as an input 

'''
first_row -- n * ("* ")
middle_row -- star spaces stars
last_row -- n * ("* ")

n = 5

i star spaces star
2  1     6     1
3  1     6     1
4  1     6     1
   
   1     6     1

first row -- n * star
last row -- n * star


n = 6

i star spaces star
2  1     8     1
3  1     8     1
4  1     8     1
5  1     8     1
   
   1     8     1

first row -- n * star
last row -- n * star

n = 4

i star spaces star
2  1     4     1
3  1     4     1
   
   1     4     1

first row -- n * star
last row -- n * star

n  hollow_spaces
4        4
5        6
6        8

hollow_spaces = 2 * n - 4 or 2 * (n - 2)
'''

n = int(input())
for i in range(1, n+1):
    if i == 1 or i == n:
        row = n * "* "
    else:
        spaces = 2 * n - 4
        row = "* " + spaces * " " + "* "
    print(row)