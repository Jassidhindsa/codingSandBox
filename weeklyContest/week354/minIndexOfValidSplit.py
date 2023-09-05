

def minIndexOfValidSplit(nums):
    from_left = [0 for i in range(len(nums))]
    from_right = [0 for i in range(len(nums))]

    local_dict = {}
    curr_max_occur_times = -1
    curr_max_occur_val = None

    for index, num in enumerate(nums):
        local_dict[num] = 1 + local_dict.get(num, 0)
        if local_dict[num] > curr_max_occur_times:
            curr_max_occur_times = local_dict[num]
            curr_max_occur_val = num
        from_left[index] = [curr_max_occur_val, curr_max_occur_times]
    
    local_dict = {}
    curr_max_occur_times = -1
    curr_max_occur_val = None

    for index, num in enumerate(nums[::-1]):
        local_dict[num] = 1 + local_dict.get(num, 0)
        if local_dict[num] > curr_max_occur_times:
            curr_max_occur_times = local_dict[num]
            curr_max_occur_val = num
        from_right[len(nums) - index - 1] = [curr_max_occur_val, curr_max_occur_times]

    
    for index in range(len(nums)-1):
        left_arr = from_left[index]
        right_arr = from_right[index+1]

        if left_arr[0] == right_arr[0] and (left_arr[1] * 2 > index+1) and (right_arr[1] * 2 > len(nums) - index - 1):
            return index
        
    return -1


if __name__ == "__main__":
    minIndexOfValidSplit([1,2,2,2])