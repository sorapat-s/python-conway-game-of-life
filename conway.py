import numpy as np
import pygame
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

FPS = 60

# drawingVariable
MARGIN_WIDTH = 50
MARGIN_HEIGHT = 50
GRID_WIDTH = 100
GRID_HEIGHT = 100
BOARD_WIDTH = int(HEIGHT-MARGIN_HEIGHT-MARGIN_HEIGHT)
BOARD_HEIGHT = int(HEIGHT-MARGIN_HEIGHT-MARGIN_HEIGHT)
CELL_WIDTH = int(BOARD_WIDTH/GRID_WIDTH)
CELL_HEIGHT = int(BOARD_HEIGHT/GRID_HEIGHT)

#color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# gameVarible
dieMin = 2
dieMax = 3
alive = 3
gameRun = 1

def draw_window():
    backBoard = pygame.Rect(MARGIN_HEIGHT-1, MARGIN_WIDTH-1, 402, 402)
    pygame.draw.rect(WIN, WHITE, backBoard)

    for x in range(0, BOARD_WIDTH, CELL_WIDTH):
        for y in range(0, BOARD_HEIGHT, CELL_HEIGHT):
            rect = pygame.Rect(x+MARGIN_WIDTH, y+MARGIN_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
            if board[int(x/CELL_WIDTH)][int(y/CELL_HEIGHT)] > 0:
                pygame.draw.rect(WIN, WHITE, rect)
            else:
                pygame.draw.rect(WIN, BLACK, rect)
    
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    global board, boardTemp
    board = np.zeros([GRID_WIDTH, GRID_HEIGHT], dtype = int)
    initialBoard = [[3,5],[3,6],[3,7],[4,7],[5,6]]
    for i in range(len(initialBoard)):
        board[initialBoard[i][0]][initialBoard[i][1]] = 1

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        draw_window()
        boardTemp = np.zeros([GRID_WIDTH, GRID_HEIGHT], dtype = int)
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
        

if __name__ == "__main__":
    main()
