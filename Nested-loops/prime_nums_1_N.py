# Write a program to print all the Prime Number from 1 to N

# A number which is completely divisible only by 1 & itself and [not completely divisible
# by any other numbers.]

# A number which has only two factors : 1 & itself

'''
Factors:
A number 'i' is a father of 'm' when 'i' divides 'm' completely
Remainder = 0
m % i = 0
i is a factor of m

n = 10
1 - 10 all the prime numbers
m = 2 3 4 5 6 7 8 9 10
    0 0    0   0        
is prime number of factors of m other 1 & m (itself)

take 8 
8 % 1 = 0
8 % 2 = 0 true
8 % 3 = 0 
8 % 4 = 0 true 
8 % 5 = 0
8 % 6 = 0
8 % 7 = 0
8 % 8 = 0 true

1, 8, 2, 4

take 7
7 % 1 = 0 true
7 % 2 = 0 
7 % 3 = 0 
7 % 4 = 0  
7 % 5 = 0
7 % 6 = 0
7 % 7 = 0 true

1, 7

n = 7
2 3 4 5 6 7

2 to n
range(2, n+1):
'''

n = int(input())
# Number of factors of all numbers from 2 to n
for m in range(2, n+1):
    num_of_factors = 0
    # number of factors of m other than 1 & m
    for i in range(2, m):
        # number of factors of m when considering i
        if m % i == 0:
            num_of_factors += 1
    if num_of_factors == 0:
        print(m)
