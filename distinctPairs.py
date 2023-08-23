

def distinctPairs(nums, difference):
    vals = set()
    count = 0

    for num in nums:    
        if num + difference in vals:
            count += 1
        if num - difference in vals:
            count += 1
        
        vals.add(num)
    
    return count