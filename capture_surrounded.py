# for https://leetcode.com/problems/surrounded-regions/

from pprint import pprint

def check_neighbours(board, i, j):
    if i>-1 and j>-1 and i<len(board) and j<len(board[0]) and board[i][j] == 'O':
        # print(board,'hi')
        board[i][j] = 1
        # print(board,'bye')
        check_neighbours(board, i-1, j)
        check_neighbours(board, i, j-1)
        check_neighbours(board, i+1, j)
        check_neighbours(board, i, j+1)

def capture_surrounded_Os(board):
    """
    board: 2d list
    modifies board in-place
    """
    if board == []:
        return
    leni = len(board)
    lenj = len(board[0])
    print('start')
    pprint(board)
    # recursively fill 'O's with 1's, starting at edges
    for i in range(leni):
        if board[i][0] == 'O':
            check_neighbours(board, i, 0)
        if board[i][lenj-1] == 'O':
            check_neighbours(board, i, lenj-1)
    for j in range(lenj):
        if board[0][j] == 'O':
            check_neighbours(board, 0, j)
        if board[leni-1][j] == 'O':
            check_neighbours(board, leni-1, j)
    print('should have more 1\'s:')
    pprint(board)
    # fill the rest with 'X's
    for i in range(leni):
        for j in range(lenj):
            if board[i][j] == 1:
                board[i][j] = 'O'
            else:
                board[i][j] = 'X'

print('\n----INPUT #1----\n')

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
capture_surrounded_Os(board)
print('final')
pprint(board)

print('\n----INPUT #2----\n')

board = [["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","O","X","X"]]
capture_surrounded_Os(board)
print('final')
pprint(board)
