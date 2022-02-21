sudoku = [ 
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

sudoku1 = [
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

sudoku2 = [
    [0,0,2,0,4,0],
    [0,0,0,0,6,0],
    [0,4,0,0,0,2],
    [0,0,0,4,0,1],
    [1,0,0,0,0,0],
    [3,0,6,0,0,0],
]

def spaceToFill(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                return (x, y)
    return None


def validation(board, number, row, col, case):
    for x in range(len(board)):
        if board[x][col] == number:
            return False
    for y in range(len(board[0])):
        if board[row][y] == number:
            return False 
    # if case == 1:
    #     for i in range(3):
    #         for j in range(3):
    #             if board[3 * (row // 3) + i][3 * (col // 3) + j] == number:
    #                 return False
    # elif case == 2:
    for i in range(4-case):
        for j in range(3):
            if board[(4-case) * (row // (4-case)) + i][3 * (col // 3) + j] == number:
                return False
    return True

def solver(board, case):
    test = spaceToFill(board)
    if not test:
        return True
    for number in range(1, (11-(case**2))):
        if validation(board, number, test[0], test[1], case):
            board[test[0]][test[1]] = number
            if solver(board, case): 
                return True
            else:
                board[test[0]][test[1]] = 0
    return False



if __name__ == '__main__':
    while True:
        boardSize = input("Type 1 for 9x9 board, type 2 for 6x6 board ")
        # boardname = "sudoku{}".format(boardSize)
        # print(boardname)
        if boardSize == "1":
            solver(sudoku1, int(boardSize))
            for line in sudoku1:
                print(line)
        elif boardSize == "2":
            solver(sudoku2, int(boardSize))
            for line in sudoku2:
                print(line)
    






