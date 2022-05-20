# Binary Search Algorithm
"""
Explanation
This algorithm is used to find the target
when an array is sorted. When we are looping the
array, every time we check the middle element of the 
arrar, and if it is not equal to the target, we remove
the half of the array.
If the target cannot be finded, then return 'Not Found'

Looping manually
ls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 1
1) mid_el = 5 -> 5 != 1 -> ls = [0, 1, 2, 3, 4], we removed the half of the array
2) mid_el = 2 -> 2 != 1 -> ls = [0, 1], we removed the half of the array
3) mid_el = 0 -> 0 != 1 -> ls = [1], we removed the half again
4) mid_el = 1 -> 1 == 1, Yeey, we found!

--- Time complexity - O(log n) -> log in basis of 2, e.g log 8 = 3
--- Space complexity - O(1)
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return f"The target is on index {mid}"
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return "Not Found"

print(binary_search(range(11), 1))
