


def containsMostWater(height):
    left_pointer = 0
    right_pointer = len(height) - 1
    max_water = 0

    while left_pointer < right_pointer:
        water = min(height[left_pointer], height[right_pointer])*(right_pointer - left_pointer)
        max_water = max(max_water, water)
        if height[left_pointer] < height[right_pointer]:
            left_pointer += 1
        else:
            right_pointer -= 1

    return max_water


if __name__ == "__main__":
    print(containsMostWater([1,8,6,2,5,4,8,3,7]))