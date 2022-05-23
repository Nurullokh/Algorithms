# Selection Sort Algorithm

"""
--- Explanation
This algorithm is used to sort the given array in ascending order.
The idea behind is to find the smallest of the array and
to append it in a new array. So, we need a helper function to find
the smallest in the array.

--- Looping manually
ls = [5, 3, 2, 6]
1) ls = [5, 3, 2, 6] -> mn = 2, new_ls = [2]
2) ls = [5, 3, 6] -> mn = 3 -> new_ls = [2, 3]
3) ls = [5, 6] -> mn = 5 -> new_ls = [2, 3, 5]
4) ls = [6] -> mn = 6 -> new_ls = [2, 3, 5, 6] -> done!

--- Time complexity - O(n^2)
--- Space complexity - O(1)
"""

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_ls = []
    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        new_ls.append(arr.pop(smallest_index))
    return new_ls

print(selection_sort([5, 3, 2, 6]))