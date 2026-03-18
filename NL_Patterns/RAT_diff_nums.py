'''
i = 0 --> n - 1
j = 0 -- i

i number
0   1
1   2
2   3
3   4
4   5
   i+1

print(i+1, end = " ")
print(str(i+1) + " ", end = "")
'''

n = int(input())
for i in range(n):
    for j in range(i+1):
        print(str(i + 1) + " ", end = "")
    print()