


def search2dMatrix(matrix, target):
    top_pointer = 0
    bottom_pointer = len(matrix) - 1

    while top_pointer <= bottom_pointer:
        mid_pointer = (top_pointer + bottom_pointer) // 2

        if matrix[mid_pointer][0] > target:
            bottom_pointer = mid_pointer - 1
        elif matrix[mid_pointer][-1] < target:
            top_pointer = mid_pointer + 1
        else:
            break
    
    if top_pointer > bottom_pointer:
        return False
    row = (top_pointer + bottom_pointer) // 2
    left_pointer, right_pointer = 0, len(matrix[0]) -  1

    while left_pointer <= right_pointer:
        mid_pointer = (left_pointer + right_pointer) // 2

        if matrix[row][mid_pointer] == target:
            return True
        elif matrix[row][mid_pointer] < target:
            left_pointer = mid_pointer + 1
        else:
            right_pointer = mid_pointer - 1
    
    return False


if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(search2dMatrix(matrix, 3))