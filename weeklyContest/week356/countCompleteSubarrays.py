

def countCompleteSubarrays(nums):

    mp1, mp2 = {}, {}

    for i in nums:
        mp1[i] = mp1.get(i, 0) + 1
    
    leading, trailing, n, final_count = 0, 0, len(nums), 0

    while leading < n:
        mp2[nums[leading]] = mp2.get(nums[leading], 0) + 1
        while len(mp2) == len(mp1):
            ans += (n - leading)

            mp2[nums[trailing]] -= 1
            if mp2[nums[trailing]] == 0:
                del mp2[nums[trailing]]
            trailing += 1
        leading += 1
    
    return final_count