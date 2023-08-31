



def maxSum(nums):
    nums_count = {}
    max_sum = -1

    for num in nums:
        string_num = str(num)
        curr_max = 1
        for char in string_num:
            curr_max = max(curr_max, int(char))
        
        if curr_max not in nums_count:
            nums_count[curr_max] = [num]
        else:
            last_max = nums_count[curr_max][0]
            if len(nums_count[curr_max]) == 1:
                max_sum = max(max_sum, num + last_max)
            else:
                second_last_max = nums_count[curr_max][1]
                if num > second_last_max:
                    max_sum = max(max_sum, num + last_max)
                    nums_count[curr_max].remove(second_last_max)

            if num > last_max:
                nums_count[curr_max].insert(0, num)
            else:
                nums_count[curr_max].append(num)
    
    return max_sum


def maxSumOptimal(nums):
    nums_count = {}
    max_sum = -1

    for num in nums:
        string_num = str(num)
        curr_max = 1
        for char in string_num:
            curr_max = max(curr_max, int(char))
        
        if curr_max not in nums_count:
            nums_count[curr_max] = num
        else:
            max_sum = max(max_sum, nums_count[curr_max] + num)
            nums_count[curr_max] = max(nums_count[curr_max], num)
    
    return max_sum

if __name__ == "__main__":
    print(maxSum([51,71,17,24,42]))