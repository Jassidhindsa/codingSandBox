


def validSudoku(board):
    set_top_left, set_top_middle, set_top_right, set_middle_left, set_middle_middle, set_middle_right, set_bottom_left, set_bottom_middle, set_bottom_right = set(),  set(), set(), set(), set(), set(), set(), set(), set()
    added_indices = set()

    def setCheck(set_to_check, value):
        if value in set_to_check:
            return True
        return False
    
    def getSet(row, col):
        if row < 3:
            if col < 3:
                return set_top_left     
            elif col < 6:
                return set_middle_left
            else:
                return set_bottom_left
        elif row < 6:
            if col < 3:
                return set_top_middle     
            elif col < 6:
                return set_middle_middle
            else:
                return set_bottom_middle
        else:
            if col < 3:
                return set_top_right       
            elif col < 6:
                return set_middle_right
            else:
                return set_bottom_right

    def rowCheck(row, value):
        rowSet = set()
        for i in range(9):
            boardVal = board[row][i]
            if boardVal != "." and (int(boardVal) > 9 or int(boardVal) < 1 or int(boardVal) in rowSet):
                return False
            elif boardVal != "." and (row, i) not in added_indices:
                associated_set = getSet(row, i)
                if setCheck(associated_set, int(board[row][i])):
                    return False
                associated_set.add(int(board[row][i]))
                added_indices.add((row, i))
            if boardVal != ".":
                rowSet.add(int(boardVal))
        return True
        
    def colCheck(col, value):
        colSet = set()
        for i in range(9):
            boardVal = board[i][col]
            if boardVal != "." and (int(boardVal) > 9 or int(boardVal) < 1 or int(boardVal) in colSet):
                return False
            elif boardVal != "." and (i, col) not in added_indices:
                associated_set = getSet(i, col)
                if setCheck(associated_set, int(boardVal)):
                    return False
                associated_set.add(int(boardVal))
                added_indices.add((i, col))
            if boardVal != ".":
                colSet.add(int(boardVal))
        return True

    for i in range(9):
        if not rowCheck(i, board[i][i]) or not colCheck(i, board[i][i]):
            return False
        elif board[i][i] != ".":
            associated_set = getSet(i, i)
            if setCheck(associated_set, board[i][i]):
                return False
            associated_set.add(board[i][i])
    
    return True

if __name__ == "__main__":
    val = [[".",".","5",".",".",".",".",".","."],
           [".",".",".","8",".",".",".","3","."],
           [".","5",".",".","2",".",".",".","."],
           [".",".",".",".",".",".",".",".","."],
           [".",".",".",".",".",".",".",".","9"],
           [".",".",".",".",".",".","4",".","."],
           [".",".",".",".",".",".",".",".","7"],
           [".","1",".",".",".",".",".",".","."],
           ["2","4",".",".",".",".","9",".","."]]
    print(validSudoku(val))