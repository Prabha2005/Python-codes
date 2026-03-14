'''
Input: [8, 3, 11, 2, 6]
Output: 2
Algorithm pattern
➡ Linear Scan
'''

def find_smallest_element(arr):
    small = arr[0]
    for i in range(len(arr)):
        if arr[i] < small:
            small = arr[i]
    return small

if __name__ == "__main__":
    arr = [8, 3, 11, 2, 6]
    print(find_smallest_element(arr))