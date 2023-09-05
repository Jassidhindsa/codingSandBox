

def maxScore(nums, x):

        even = nums[0] if (nums[0] % 2 == 0) else float('-inf')
        odd = nums[0] if (nums[0] % 2 != 0) else float('-inf')

        for right in range(1,len(nums)):
            cur = nums[right]
            if cur % 2 == 0:
                even = max(even,odd-x)+cur
            else:
                odd = max(even-x,odd)+cur

        return max(odd,even)