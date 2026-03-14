'''
4️⃣ Count Even Numbers
Input: [1,2,3,4,5,6]
Output: 3

Algorithm pattern
➡ Condition Count Pattern
'''


def count_of_even_element(arr):
    count = 0
    for i in arr:
        if i % 2 == 0:
            count += 1
    return count

if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    print(count_of_even_element(arr))