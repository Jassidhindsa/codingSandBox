



def threeSum(nums):
    three_sum_list = []
    nums.sort()


    for index, num in enumerate(nums):
        if index > 0 and num == nums[index - 1]:
            continue
        left_pointer = index + 1
        right_pointer = len(nums) - 1

        while left_pointer < right_pointer:
            sum_val = num + nums[left_pointer] + nums[right_pointer]
            if sum_val == 0:
                three_sum_list.append([num, nums[left_pointer], nums[right_pointer]])
                left_pointer += 1
                while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer - 1]:
                    left_pointer += 1
            elif sum_val < 0:
                left_pointer += 1
            else:
                right_pointer -= 1
    return three_sum_list


if __name__ == "__main__":
    print(threeSum([-1,0,1,2,-1,-4]))