
# Create dict for indices for each num
# iterate over each key
# add first index + len(nums) because after the last index we are coming back to the first index (circular arr)
# iterate over indices
# find the longest gap between consecutive indices
# divide that longest gap by 2 because with each step/sec we can divide the gap in half
# find the min among all the (longest gap // 2)
def minimumSeconds(nums):
    nums_indices_dict = {}
    final_min = float('inf')

    for index, num in enumerate(nums):
        if not num in nums_indices_dict:
            nums_indices_dict[num] = [index]
        else:
            nums_indices_dict[num].append(index)
    
    for key in nums_indices_dict.keys():
        nums_indices_dict[key].append(nums_indices_dict[key][0] + len(nums))
        longest = -1
        for index in range(len(nums_indices_dict[key]) - 1):
            first = nums_indices_dict[key][index]
            second = nums_indices_dict[key][index+1]
            longest = max(longest, second - first)
        final_min = min(final_min, longest // 2)
    
    return final_min
