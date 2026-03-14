# Write a program to print M pattern of N rows using starts *, where integer N is given as an input

'''
no_of spaces % 4 + i = n
no_of_spaces % 4 = n - i
no_of_spaces = 4(n-i)
row = initial_stars + "* " + spaces + " " + final * "* " 
'''

n = int(input())
for i in range(1, n+1):
    spaces = 4 * (n - i)
    initial_stars = i
    final_stars = i
    rows = initial_stars * "* " + spaces * " " + final_stars * "* "
    print(rows)