def n_Queens(N):
    '''
    Returns an NxN board with N-queens placed in correct positions.
    '''
    board = [N * [0] for _ in range(N)]
    def isAttacked(row,col,board,N):
        columns = [board[_][col] for _ in range(N)]
        rows = board[row]
        if 1 in rows or 1 in columns:
            return True
        #check left diagonal  going up -> upper left
        rowLd, colLd = row, col
        while rowLd >0 and  colLd > 0:
            if board[rowLd - 1][colLd - 1 ] == 1:
                return True
            rowLd -= 1
            colLd -= 1
        # check left diagonal going down -> lower-right
        rowLd, colLd = row, col
        while rowLd < N - 1 and colLd < N - 1:
            if board[rowLd + 1][colLd + 1] == 1:
                return True
            rowLd += 1
            colLd += 1
        # check right diagonal going down -> lower-left
        rowLd, colLd = row, col
        while rowLd < N - 1 and colLd > 0:
            if board[rowLd + 1][colLd - 1] == 1:
                return True
            rowLd += 1
            colLd -= 1
        # check right diagonal going up -> upper-right
        rowLd, colLd = row, col
        while rowLd > 0 and colLd < N - 1:
            if board[rowLd - 1][colLd + 1] == 1:
                return True
            rowLd -= 1
            colLd += 1
        #diagonals are clear
        return False


    def solve_n_Queens(board, row, N, remaining):
        if (remaining == 0):
            return True
        for col in range(N):
            #check to see if it is attacked
            if isAttacked(row,col,board,N):
                continue
            else:
                # Place the queen and recursively solve for remaining queens
                board[row][col] = 1
                if (solve_n_Queens(board, row + 1, N, remaining - 1)):
                    return True
                # backtrack if any placement results in no solution
                board[row][col] = 0
        return False
    if solve_n_Queens(board,0,N,N):
        return board
    else:
        return None
answer  = n_Queens(4)
for _ in range(len(answer)):
    print(answer[_])
