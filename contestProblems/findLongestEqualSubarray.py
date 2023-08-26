

def findLongestEqualSubarray(nums, k):
    max_length = 0
    nums_dict = {}

    for index, num in enumerate(nums):
        if num not in nums_dict:
            nums_dict[num] = [index]
        else:
            nums_dict[num].append(index)
    
    print(nums_dict)
    for num in nums_dict.keys():
        skips = []
        indices = []

        for index, val in enumerate(nums_dict[num]):
            print(val)
            if not indices:
                indices.append(index)
            else:
                skips_made = val - nums_dict[num][indices[-1]] - 1
                skips_made_so_far = sum(skips)
                if skips_made + skips_made_so_far <= k:
                    print(skips, indices, skips_made, skips_made_so_far, val)
                    if skips_made > 0:
                        skips.append(skips_made)
                    indices.append(index)
                    max_length = max(max_length, len(indices))
                else:
                    while indices and skips_made + skips_made_so_far > k:
                        if skips and len(indices) > 1 and indices[0] != indices[1]:
                            skips = skips[1:]
                        indices = indices[1:]
                        skips_made = skips_made if indices else 0
                        skips_made_so_far = sum(skips)
                        print(skips, indices, skips_made, skips_made_so_far, val)
                    if skips_made + skips_made_so_far <= k:
                        if skips_made > 0:
                            skips.append(skips_made)
                        indices.append(index)
                        max_length = max(max_length, len(indices))

        max_length = max(max_length, len(indices))
    return max_length



if __name__ == "__main__":
    nums = [7,1,1,5,5,9,1,2,10,4,7,9,1,2,5,1,5,5,4,3,5,7,1,9,6,5,10,1,9,6,1,10,7,7,7]
    print(findLongestEqualSubarray(nums, 10))