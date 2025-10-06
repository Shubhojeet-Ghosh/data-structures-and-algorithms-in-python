# ==============================================
# BIG O NOTATION — TIME + SPACE COMPLEXITY NOTES
# ==============================================

# 1. Linear Time — O(n)
def print_items(arr):
    for item in arr:
        print(item)
# ➤ Time Complexity: O(n)
#   Loop executes once per element.
#   If n doubles, time doubles.
# ➤ Space Complexity: O(1)
#   Only loop variable stored; no extra data structures used.


# 2. Quadratic Time — O(n²)
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)
# ➤ Time Complexity: O(n²)
#   Outer loop n × Inner loop n = n² operations.
# ➤ Space Complexity: O(1)
#   Constant extra memory for i and j.


# 3. Linear (skipping elements) — O(n)
def print_half(arr):
    i = 0
    while i < len(arr):
        print(arr[i])
        i += 2
# ➤ Time Complexity: O(n)
#   Runs about n/2 times → constants ignored → O(n).
# ➤ Space Complexity: O(1)
#   Only variable i stored.


# 4. Logarithmic Time — O(log n)
def log_example(n):
    i = 1
    while i < n:
        print(i)
        i *= 2
# ➤ Time Complexity: O(log n)
#   i doubles each time → 2^k = n → k = log₂(n) steps.
# ➤ Space Complexity: O(1)
#   Only i stored; no growing data structure.


# 5. Mixed Linear + Logarithmic — O(n log n)
def mix_loop(n):
    for i in range(n):          # runs n times
        j = 1
        while j < n:            # runs log n times
            print(i, j)
            j *= 2
# ➤ Time Complexity: O(n log n)
#   n outer × log n inner iterations.
# ➤ Space Complexity: O(1)
#   Only i and j variables.


# 6. Multi-variable Complexity — O(n * m)
def process(n, m):
    for i in range(n):
        for j in range(m):
            print(i, j)
# ➤ Time Complexity: O(n * m)
#   Outer loop runs n times, inner runs m times → n × m.
# ➤ Space Complexity: O(1)
#   Only constant variables used.


# 7. Binary Search — O(log n)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
# ➤ Time Complexity: O(log n)
#   Search space halves each step (n → n/2 → n/4 …).
# ➤ Space Complexity: O(1)
#   Iterative version uses fixed variables; no recursion stack.


# 8. Hashing / Hash Set Search — O(n)
def has_duplicate_hashset(arr):
    seen = set()  # Python set uses a hash table
    for x in arr:
        if x in seen:  # average O(1) membership test
            return True
        seen.add(x)
    return False
# ➤ Time Complexity: O(n)
#   Each lookup & insert = O(1) average, repeated n times → O(n).
#   Worst case (all collisions): O(n²), but rare with good hashing.
# ➤ Space Complexity: O(n)
#   Need to store up to n unique elements in the set.
