

def minimumSumOfKAvoidingArray(n, k):
    total_sum = 0
    nums_set = set()
    num = 1
    
    while len(nums_set) < n:
        if k - num not in nums_set:
            nums_set.add(num)
            total_sum += num
        num += 1
    
    return total_sum



if __name__ == "__main__":
    print(minimumSumOfKAvoidingArray(5, 4))