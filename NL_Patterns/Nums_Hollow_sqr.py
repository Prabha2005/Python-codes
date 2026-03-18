'''
Write a program to print a Hollow square of N rows and N columns using
Numbers, where interger N is given as an input
input -- no of rows?
Identify elements in the patterns

i -- 1 to N
index - indices
i j
1 1
0 0
edge or boundary
outer cell - "numbers_" ---> i = 1 or i = n or j = 1 or j = n
inner cell - "_ _"
'''
'''
n = int(input())
for i in range(1,n+1):
    for j in range(1, n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print(str(j) + " ", end = "")
        
        else:
            print(" ", end=" ")
    print()
'''
n = int(input())
for i in range(1,n+1):
    row = ""
    for j in range(1, n+1):
        if i == 1 or i == n or j == 1 or j == n:
            row = row + str(j) + " "
        
        else:
            row = row + "  "
    print(row)