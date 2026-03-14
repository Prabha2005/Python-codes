# Write a program to print a diamond of 2 * n - 1 rows using stars (*), where integer n is given as an input

'''
# TOP POSTION
i spaces stars
1   3      1
2   2      2
3   1      3
4   0      4
   (n - i) i

spaces + i = n
spaces = n - i 

# BOTTOM POSITION
i spaces stars
1     1    3
2     2    2
3     3    1
      i  
stars = i + 1
stars = n - i
'''

n = int(input())
# TOP POSTION

for i in range(1, n+1):
    spaces = (n - i)
    stars = i
    rows = spaces * " " + stars * "* "
    print(rows)

# BOTTOM POSTION
for i in range(1, n):
    spaces = i
    stars = (n - i)
    rows = spaces * " " + stars * "* "
    print(rows)