
# Works when the elemetns of the array are in between 0 and c.
# Time complexity: O(n)

def countingSort(nums):
    max_val = max(nums)

    bookkeeping_arr = [0  for i in range(max_val+1)]

    for val in nums:
        bookkeeping_arr[val] += 1
    
    sorted_arr = []

    for index, val in enumerate(bookkeeping_arr):
        val_arr = [index for i in range(val)]
        sorted_arr.extend(val_arr)

    return sorted_arr