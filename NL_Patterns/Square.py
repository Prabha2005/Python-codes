'''
n = 4
i = 0, 1, 2, 3
j = 0, 1, 2, 3

i j
0 0  * * * *
  1
  2
  3
1 0  * * * *
  1
  2
  3
2 0  * * * *
  1
  2
  3
3 0  * * * *
  1
  2
  3

* * * *
* * * *
* * * *
* * * *
'''


n = int(input())
for i in range(n): # Outer Loop
    for j in range(n): # Inner Loop
        print("*", end=" ")
    print()

    19.06