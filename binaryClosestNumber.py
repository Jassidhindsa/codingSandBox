


def binaryClosestNumber(nums, target):

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return nums[mid]
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    if right == -1:
        return nums[left]
    elif left == len(nums):
        return nums[right]
    elif abs(target - nums[left]) < abs(target - nums[right]):
        return nums[left]
    else:
        return nums[right]


if __name__ == "__main__":
    print(binaryClosestNumber([1,4,5,6,7,9], 10))