'''
j(max) = i
i = 0 --> n - i
j = 0 --> i

print(j+1, end=" ")
range(i+1)
'''

n = int(input())
for i in range(n):
    for j in range(i+1):
        print(j+1, end=" ")
    print()