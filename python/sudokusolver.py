def main():
    sudoku = [
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0]
        ]

    printTable(sudoku)
    solve(sudoku)

def solve(sudoku):
    while checkComplete(sudoku) is False:
        break

def checkComplete(sudoku):
    # check rows for completion
    for i in range(9):
        if checkRowComplete(i, sudoku) is False:
            return False

    # check columns for completion
    for j in range(9):
        if checkColComplete(j, sudoku) is False:
            return False

    # check 3x3 squares for completion
    # for k in range(9):
    #     if checkSquareComplete() is False:
    #         return False

    return True
        
def printTable(sudoku):
    for i in range( len(sudoku) ):
        for j in range( len(sudoku[i]) ):
            if j % 3 == 0:
                print('|', end='')
            if sudoku[i][j] == 0:
                print(' ', end='')
                continue
            print(sudoku[i][j], end='')
        if (i + 1) % 3 == 0:
            print()
            print('____________')
        print()

def checkSquare(num, row1, row2, col1, col2, sudoku):
    for i in range(row1, row2 + 1):
        for j in range(col1, col2 + 1):
            if sudoku[i][j] == num:
                return True

    return False

def checkRow(num, row, sudoku):
    for i in range( len(sudoku) ):
        if sudoku[row][i] == num:
            return True

    return False

def checkCol(num, col, sudoku):
    for i in range( len(sudoku) ):
        if sudoku[i][col] == num:
            return True

    return False

def checkSquareComplete(row1, row2, col1, col2, sudoku):
    num_complete = [False, False, False, False, False, False, False, False, False]
    for h in range(9):
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                if sudoku[i][j] == h + 1:
                    num_complete[h] = True

    for k in num_complete:
        if k is False:
            return False
        
    return True

def checkRowComplete(row, sudoku):
    num_complete = [False, False, False, False, False, False, False, False, False]
    for i in range( len(sudoku) ):
        for j in range( len(sudoku[row]) ):
            if sudoku[row][j] == i + 1:
                num_complete[i] = True

    for k in num_complete:
        if k is False:
            return False

    return True

def checkColComplete(col, sudoku):
    num_complete = [False, False, False, False, False, False, False, False, False]
    for i in range(9):
        for j in range(9):
            if sudoku[j][col] == i + 1:
                num_complete[i] = True

    for k in num_complete:
        if k is False:
            return False

    return True

if __name__ == '__main__':
    main()