# Quick Sort Algorithm

"""
--- Explanation
This algorithm is used to sort the array in an ascending order.
And most popular programming languages use this algo as a built-in
sorting function.
The idea behind is using D&C (Divide and conquer) method. This method is
like finding the smallest case like base case to solve the problem and
use it for the whole problem with recursion. The base case for sorting 
an array is when the array have 1 or no element, because when an 
array has 1 or 0 element, it is already sorted. And the next step is 
to find the pivot number and we find the less than pivot and the more than 
pivot and use the recursion to find the sorted array.

--- How it works
ls = [5, 3, 2, 6]
1) pivot = 5, less = [3, 2], greater = [6] and the greater is already sorted
2) ls = [3, 2] -> pivot = 3, less = [2] and greater = [], and both are sorted
3) new_ls = [2] + [3] + [] -> [2, 3]
4) ans = [2, 3] + [5] + [6] -> [2, 3, 5, 6] done!

--- Time complexity - O(n * log n) in most cases, but the worst - O(n^2),
but the worst case is rare.
--- Space complexity - O(log n), because it uses recursion, but the worst case - O(n)
"""

def quick_sort(arr):
    # base case
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr if i < pivot]
        greater = [i for i in arr if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([5, 3, 2, 6]))