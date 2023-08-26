
def findMinInRotatedSortedArray(nums):
    left_pointer, right_pointer = 0, len(nums) - 1
    final_min = float("inf")

    while left_pointer < right_pointer:
        mid_pointer = (left_pointer +  right_pointer) // 2

        final_min = min(final_min, nums[mid_pointer])

        if nums[mid_pointer] > nums[right_pointer]:
            left_pointer = mid_pointer + 1
        else:
            right_pointer = mid_pointer - 1
    
    final_min = min(final_min, nums[left_pointer])
    return final_min


if __name__ == "__main__":
    print(findMinInRotatedSortedArray([3,4,5,1,2]))