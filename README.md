# Python Coding Practice & DSA
A collection of Python programs solved during coding practice and technical interview preparation.

## Topics Covered
- Python Fundamentals
- Arrays and Lists
- String Manipulation
- Recursion
- Searching and Sorting
- Greedy Algorithms
- Linked Lists
- Binary Trees (Traversals & Problems)
- Mathematical and Logical Problems
- Interview & Competitive Programming Challenges

## Problem Types
- Maximum subarray and budget problems
- Work allocation and scheduling
- Tree-based problems and traversals
- Linked list operations
- Logic and constraint-based problems
- Real-world interview-style challenges

## Structure
Each folder/file represents an independent problem solution with a clear problem statement and Python implementation.

## How to Run
1. Install Python 3
2. Clone the repository
3. Run any file using: `python filename.py`

## Purpose
This repository reflects my continuous learning, logical thinking, and preparation for coding interviews and assessments.

## Learning Path
Problems are organized from basic Python logic to advanced data structure and interview-level challenges.
1. Python Basics & Logical Problems  
2. Arrays and List-Based Problems  
3. String Manipulation  
4. Searching & Greedy Techniques  
5. Linked List  
6. Recursion  
7. Binary Trees  
8. Graph / Grid / Forest-Based Problems  
9. Revision & Contest Problems

## 1️⃣ Python Basics & Warm-up Logic (Start here – shows fundamentals)
1. Single Ton
2. Sum of proper divisors
3. Triangle Area Validation in 2D Plane
4. Magical Number System
5. Stationery Shop
6. Pizza Party (ICS-4)

## 2️⃣ Arrays & List-Based Problems- (Core interview area)
* Work Allocate Sum
* Work Allocate (Job Scheduling)
* Maximum Toys (Subarray Budget Problem)
* Longest Subarray with Sum ≤ K
* Coin Change (Greedy)
* Ravi’s Coding Marathon

## 3️⃣ Strings & Pattern Logic - (Logic + implementation skills)
1. Password Generator
2. Card Shuffle Challenge
3. Identity Correct Operator
4. String-based Single Ton / Pattern problems

## 4️⃣ Searching, Sorting & Greedy Techniques - (Efficiency + thinking)
* Coin Change (Greedy revisit)
* Budget & Allocation optimization problems
* Constraint-based maximum / minimum problems

## 5️⃣ Linked List - (Data structure transition)
1. Kosakas Linked List
2. Linked List creation
3. Linked List insert / delete operations

## 6️⃣ Recursion Fundamentals - (Foundation for trees)
* Recursive sum / traversal logic
* Recursive subarray / decision problems

## 7️⃣ Trees (Very Important for Coding Rounds) - (Advanced but expected)
1. Take Input Level Wise of Binary Tree
2. Binary Tree Traversals
3. Inorder
4. Preorder
5. Postorder
6. Level Order
7. Enchanted Forest Tree Swap

## 8️⃣ Graph / Grid / Forest Logic (Problem-Solving Heavy) - (Advanced reasoning)
* Forest Explorer
* Forest of Eldoria
* Safe Place of King
* Policemen – Thieves

## 9️⃣ Revision & Contest Problems - (Shows seriousness & consistency)
--> Last Time Revision Sheet
--> Ravi’s Coding Marathon
--> Maximum Toys (Revised / Optimized)

## Author
Lakshmi Prabha V  
Python | DSA | Problem Solving

# 📌 FINAL REVISION SHEETS (Last-Minute Interview Prep)

Save this section. Read once before exams/interviews. Enough.

# 🧠 Sliding Window — Final Revision

When to use
Subarray / Substring
Continuous elements
Max / Min / Longest / Smallest

✔ If all appear → Sliding Window
Core Idea
Reuse previous computation.
👉 Add right, remove left.

Two Types
Fixed Window → size k given
Variable Window → condition based

Golden Template

left = 0
current = 0
ans = 0

for right in range(n):
    current += arr[right]

    while condition_breaks:
        current -= arr[left]
        left += 1

    ans = max(ans, right - left + 1)

🔒 Memory lock: Expand → Shrink → Update

# 🧠 Subarrays — One-Page Concept Lock
Definition
A subarray is always continuous.
❌ [1,3] → not subarray
✅ [2,3] → subarray

Total subarrays
n * (n + 1) / 2

Technique Decision
Question	Use
Print / Count	2 loops
Max / Min / Longest	Sliding Window
Sum = K (exact)	Prefix Sum

🔒 Memory:
Subarray = stays together
🧠 Graph, BFS & DFS — Final Lock

# Graph
Nodes + Edges
Directed / Undirected
Weighted / Unweighted

BFS
Queue
Shortest path
Level order

from collections import deque
q = deque([start])
visited = set([start])
while q:
    node = q.popleft()
    for nei in graph[node]:
        if nei not in visited:
            visited.add(nei)
            q.append(nei)


# DFS
Stack / Recursion
Path / Cycle / Components

def dfs(node):
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs(nei)

🔒 Rule
Shortest path → BFS
Deep traversal → DFS
