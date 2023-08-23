
import heapq

def trappingRainWater(height):
    total_water = 0
    if not height or len(height) <= 1:
        return 0
    
    left_pointer = 0
    right_pointer = len(height) - 1
    left_max = height[left_pointer]
    right_max = height[right_pointer]

    while left_pointer < right_pointer:
        if left_max < right_max:
            left_pointer += 1
            left_max = max(left_max, height[left_pointer])
            total_water += left_max - height[left_pointer]
        else:
            right_pointer -= 1
            right_max = max(right_max, height[right_pointer])
            total_water += right_max - height[right_pointer]
    
    return total_water


if __name__ == "__main__":
    print(trappingRainWater([4,2,0,3,2,5]))