'''
7️⃣ Reverse an Array
Input:  [1,2,3,4]
Output: [4,3,2,1]

Algorithm pattern
➡ Two Pointer Swap

'''


def reverse_arr(arr):
    low = 0
    high = len(arr) - 1
    while low<high:
        temp = arr[low]
        arr[low] = arr[high]
        arr[high] = temp
    return arr

if __name__ == "__main__":
    arr = [1,2,3,4]
    print(reverse_arr(arr))