# Write a program to print a Hollow Right Angle Triangle of N rows using numbers starting
# from 1, where integer N is given as input

'''
i j
1 1
2 1(2)
3 1(3)
4 1(4)

j = 1 to N

last_row = i == n
diagonal_row = 

i = j or j = 1

i = 1 to N
  j = 1 to i
    if i == j or j == 1 or i == n
       print(num, end = " ")
       num = num + 1
    else:
       print(" ", end = " ")

  print()

'''
n = int(input())
num = 1
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j or j == 1 or i == n:
            print(num, end = " ")
            num += 1
        else:
            print(" ", end = " ")
    print()
