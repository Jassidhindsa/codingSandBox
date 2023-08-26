

def binarySearch(nums, target):
    left_pointer = 0
    right_pointer = len(nums) - 1

    while left_pointer <= right_pointer:
        mid_pointer = (left_pointer + right_pointer) // 2

        if nums[mid_pointer] == target:
            return mid_pointer
        elif nums[mid_pointer] < target:
            left_pointer = mid_pointer + 1
        else:
            right_pointer = mid_pointer - 1
    
    return -1

if __name__ == "__main__":
    print(binarySearch([-1,0,3,5,9,12], 9))