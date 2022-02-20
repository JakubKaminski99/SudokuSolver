sudoku = [
    [8,0,0,2,0,0,0,0,0], #0
    [0,0,0,0,0,0,0,8,5], #1
    [0,0,0,6,0,4,3,0,0], #2
    [0,0,0,9,0,1,7,0,0], #3 0
    [9,3,0,5,0,0,6,0,4], #4 1
    [0,7,0,0,0,0,0,2,0], #5 2
    [0,0,0,0,0,9,0,0,0], #6 0
    [0,0,7,0,0,0,0,6,0], #7 1
    [0,1,3,7,0,0,5,0,0]  #8 2
]

sudoku1 = [ 
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]


def spaceToFill(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                return (x, y)
    return None


def validation(board, number, row, col):
    for x in range(len(board)):
        if board[x][col] == number:
            return False
    for y in range(len(board[0])):
        if board[row][y] == number:
            return False 
    for i in range(3):
        for j in range(3):
            if board[3 * (row // 3) + i][3 * (col // 3) + j] == number:
                return False
    return True

def solver(board):
    test = spaceToFill(board)
    if not test:
        return True
    for number in range(1, 10):
        if validation(board, number, test[0], test[1]):
            board[test[0]][test[1]] = number
            if solver(board): 
                return True
            else:
                board[test[0]][test[1]] = 0
    return False



if __name__ == '__main__':
    solver(sudoku)
    for line in sudoku:
        print(line)






