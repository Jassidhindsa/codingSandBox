
# confusion was that i < j but when we pick items even if sorted the i < j will still satisfy.
def countPairs(nums, target):
        nums.sort()
        count = 0
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] + nums[right] < target:
                count += (right - left )
                left += 1
            else:
                right -= 1
        
        return count

# maintaing a monotonic stack and using that stack finding the count

        # nums_stack = []
        # count = 0
        
        # for num in nums:
        #     if not nums_stack:
        #         nums_stack.append(num)
        #     else:

        #         def maintainStack(rem_stack):
        #             if not rem_stack:
        #                 return 0
        #             else:
        #                 last_val = rem_stack[-1]

        #                 if last_val + num < target:
        #                     rem_stack.pop()
        #                     local_count = maintainStack(rem_stack)
        #                     rem_stack.append(last_val)
        #                     return 1 + local_count
        #                 else:
        #                     return 0

        #         def addToStack(rem_stack):
        #             if not rem_stack:
        #                 rem_stack.append(num)
        #                 return
        #             elif rem_stack[-1] > num:
        #                 rem_stack.append(num)
        #                 return 
        #             else:
        #                 popped_val = rem_stack.pop()
        #                 addToStack(rem_stack)
        #                 rem_stack.append(popped_val)
        #                 return
        #         count += maintainStack(nums_stack) 
        #         addToStack(nums_stack)
        
        # return count