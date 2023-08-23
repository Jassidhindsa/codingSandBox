

def twoSumIfSorted(numbers, target):
    left_pointer, right_pointer = 0, len(numbers) - 1

    while left_pointer < right_pointer:
        sum_of_left_and_right = numbers[left_pointer] + numbers[right_pointer]
        if sum_of_left_and_right == target:
            return [left_pointer, right_pointer]
        elif sum_of_left_and_right < target:
            left_pointer += 1
        else:
            right_pointer -= 1
    
    return [-1]


if __name__ == "__main__":
    print(twoSumIfSorted([2,7,11,15], 9))