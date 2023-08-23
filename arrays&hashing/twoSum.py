


def twoSum(nums, target):
    indices_dict = {}

    for index, val in enumerate(nums):
        if target - val in indices_dict:
            return [indices_dict[target - val], index]
        indices_dict[val] = index
    
    return [-1]



if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))