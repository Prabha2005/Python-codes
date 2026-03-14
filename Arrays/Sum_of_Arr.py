'''Write a Python program to sum all the items in an array.
Input: [1,2,3,4,5]
Output: 15
Algorithm pattern
➡ Accumulator Pattern
'''


def sum_of_element(arr):
    add = 0
    for i in arr:
        add += i
    return add
    

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(sum_of_element(arr))