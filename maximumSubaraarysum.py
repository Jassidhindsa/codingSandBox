#Given an array of n numbers, our task is to calculate the maximum subarray sum, i.e., the largest possible sum of a sequence of consecutive values in the
#array

# Approach 1
# Time complexity: O(n^2)

def brute_force_max_subarray(nums):
    max_sum = 0

    for i in range(len(nums)):
        local_sum = 0
        for j in range(i, len(nums)):
            local_sum += nums[j]
            max_sum = max(max_sum, local_sum)
    
    return max_sum

# Approach 2
# Time Complexity: O(n)

def optimal_max_subarray(nums):
    max_sum = 0
    local_sum = 0

    for i in range(len(nums)):
        local_sum = max(nums[i], nums[i]+local_sum)
        max_sum = max(max_sum, local_sum)
    
    return max_sum