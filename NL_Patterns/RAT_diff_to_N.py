'''
i = 0 --> n - 1
j = 0 -- i
print(k, end = " ")
k = k + 1 or k += 1
'''

n = int(input())
k = 1
for i in range(n):
    for j in range(i+1):
        print(str(k) + " ", end = "")
        k += 1
    print()