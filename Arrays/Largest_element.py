'''
Input: [3, 7, 2, 9, 5]
Output: 9
Algorithm pattern
➡ Linear Scan
'''
def find_largest_element(arr):
    large = arr[0]
    for i in range(len(arr)):
        if arr[i] > large:
            large = arr[i]
    return large

if __name__ == "__main__":
    arr = [3, 7, 2, 9, 5]
    print(find_largest_element(arr))