
#Monotonic stack
def maxArrayValue(nums):
        stack = []
        nums = nums[::-1]
        for num in nums:
            while stack and stack[-1] >= num:
                num += stack.pop()
            
            stack.append(num)
        
        return stack[-1]