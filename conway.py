import numpy as np

# gameVarible
dieMin = 2
dieMax = 3
alive = 3
gameRun = 1
GRID_WIDTH = 20
GRID_HEIGHT = 20
run = 1

board = np.zeros([GRID_WIDTH, GRID_HEIGHT], dtype = int)
boardTemp = np.zeros([GRID_WIDTH, GRID_HEIGHT], dtype = int)

def printBoard():
    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            if board[i][j] > 0:
                print('O', end = '')
            else:
                print(' ', end = '')
        print('')

initialBoard = [[3,5],[3,6],[3,7],[4,7],[5,6]]

for i in range(len(initialBoard)):
    board[initialBoard[i][0]][initialBoard[i][1]] = 1
printBoard()
if input("continue?\n") == 'n':
    run = 0

while run:
    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            neighborSum = 0
            for ii in range(i-1,i+2):
                for jj in range(j-1,j+2):
                    neighborSum += board[ii%GRID_WIDTH][jj%GRID_HEIGHT]>0
            neighborSum -= board[i][j]>0
            if neighborSum == alive:
                boardTemp[i][j] = 1
            if dieMin <= neighborSum <= dieMax and board[i][j] == 1:
                boardTemp[i][j] = 1
    board = boardTemp
    boardTemp = np.zeros([GRID_WIDTH, GRID_HEIGHT], dtype = int)
    printBoard()
    if input("continue?\n") == 'n':
        run = 0


