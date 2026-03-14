# Right Angle Triangle Mirror Pattern 

n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    spaces = 2 * (n - i)
    stars = i
    rows = spaces * " " + "* " * stars

    print(rows)