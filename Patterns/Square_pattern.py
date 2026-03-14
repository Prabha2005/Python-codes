'''
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

'''

n = int(input("Enter the number of rows: "))
# for i in range(n):
for i in range(1, n + 1):
    rows = "* " * n
    print(rows)