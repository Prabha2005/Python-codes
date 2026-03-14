'''
5️⃣ Search Element (Linear Search)

Return True / False if element exists.

Input:
arr = [10,20,30,40]
target = 30

Output: True

Algorithm pattern
➡ Linear Search
'''


def search_element(arr, target):
    return True if target in arr else False

if __name__ == "__main__":
    arr = [10,20,30,40]
    target = 30
    print(search_element(arr, target))