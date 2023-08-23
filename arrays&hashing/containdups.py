

def containdups(nums):
    nums_set = set()

    for num in nums:
        if num in nums_set:
            return True
        nums_set.add(num)
    return False





if __name__ == "__main__":
    print(containdups([1,2,3,4]))