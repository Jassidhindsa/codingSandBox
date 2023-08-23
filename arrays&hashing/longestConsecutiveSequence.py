


def longestConsecutive(nums):
        worth_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in worth_set:
                local_longest = 1
                local_num = num + 1
                while local_num in worth_set:
                    local_longest += 1
                    local_num += 1
                longest = max(longest, local_longest)
        
        return longest



if __name__ == "__main__":
     print(longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))