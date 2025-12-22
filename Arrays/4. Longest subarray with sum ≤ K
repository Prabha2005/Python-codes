Longest subarray with sum ≤ K

Problem Statement
Given an array of positive integers nums and an integer K, find the length of the longest contiguous subarray whose sum is less than or equal to K.

Input Format
The first line contains an integer n, the number of elements in the array.
The second line contains n space-separated integers representing the array nums.
The third line contains an integer K.

Output Format
Print a single integer — the maximum length of a subarray whose sum is ≤ K.

Constraints
1 ≤ n ≤ 10⁵
1 ≤ nums[i] ≤ 10⁵
1 ≤ K ≤ 10⁹

Example 1
Input
6
2 1 5 1 3 2
7

Output
3

Explanation
The subarray [1, 5, 1] has sum 7, which is ≤ K and has maximum length.

Example 2
Input
5
1 2 3 4 5
9
Output
3
Explanation
The subarray [2, 3, 4] has sum 9.

Python 3:
n = int(input())
arr = [int(digit) for digit in input().split()][:n]
k = int(input())

left = 0
res = 0
max_len = 0
for right in range(n):
    res += arr[right]
    while res > k:
        res -= arr[left]
        left += 1
    max_len = max(max_len, right - left + 1)
print(max_len)

