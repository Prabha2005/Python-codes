'''
from ast import pattern


6️⃣ Count Occurrence of an Element
Input:
arr = [1,2,3,2,4,2]
target = 2

Output: 3

Algorithm pattern
➡ Frequency Count

'''

def count_occurance(arr, target):
    count = 0
    for i in arr:
        if i == target:
            count += 1
    return count

if __name__ == "__main__":
    arr = [1,2,3,2,4,2]
    target = 2
    print(count_occurance(arr, target))