'''
Connect4Minimax.py is a minimax algorithm for playing
connect 4
3/11/22
author = CharlotteMiller
'''

import pygame
import numpy
import time
import random

background_color = (234, 212, 252)
red_color = (255, 26, 26)
yellow_color = (250, 255, 77)
pygame.init()
pygame.font.init()
favFont = pygame.font.Font('freesansbold.ttf', 70)
player = 1


def gameSetup():
    global screen, board, player, running
    screen = pygame.display.set_mode(size=(1000, 875))
    screen.fill(background_color)
    pygame.display.set_caption("Connect 4")
    # board
    pygame.draw.rect(surface=screen, color=(4, 14, 149), rect=(50, 50, 900, 775))
    for i in range(1, 8):
        pygame.draw.circle(surface=screen, color=(234, 212, 252), center=(125 * i, 125), radius=50)
        pygame.draw.circle(surface=screen, color=(234, 212, 252), center=(125 * i, 250), radius=50)
        pygame.draw.circle(surface=screen, color=(234, 212, 252), center=(125 * i, 375), radius=50)
        pygame.draw.circle(surface=screen, color=(234, 212, 252), center=(125 * i, 500), radius=50)
        pygame.draw.circle(surface=screen, color=(234, 212, 252), center=(125 * i, 625), radius=50)
        pygame.draw.circle(surface=screen, color=(234, 212, 252), center=(125 * i, 750), radius=50)
    textPrinting("Red Turn", 500, 25, color(player))
    pygame.display.flip()
    running = True
    pygame.display.update()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                turn()


def createIntBoard():
    global board
    board = numpy.zeros((7, 6))
    global boardCol
    boardCol = (125, 250, 375, 500, 625, 750, 875)
    global boardRow
    boardRow = (125, 250, 375, 500, 625, 750)
    # each array is a column, numbered 0-6 with rows numbered 0-5 in each column


# drops piece of player's color at
# player shows whether current player is red or yellow
def dropPiece(player, col, row):
    board[col][row] = player
    pygame.draw.circle(surface=screen, color=color(player), center=(boardCol[col], boardRow[row]), radius=50)
    pygame.display.update()


# whenever text must be had
def textPrinting(text, cx, cy, colour):
    global favFont
    thing = favFont.render(text, True, colour)
    textRect = thing.get_rect()
    textRect.center = (cx, cy)
    screen.blit(thing, textRect)


# check if there is a connect 4 yet
def gameWon():
    # horizontal win
    for i in range(0, 4):
        for j in range(0, 6):
            if board[i][j] != 0 and board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j]:
                return True
    # vertical win
    for j in range(0, 3):
        for i in range(0, 7):
            if board[i][j] != 0 and board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3]:
                return True
    # + diagonal win
    for i in range(0, 4):
        for j in range(0, 3):
            if board[i][j] != 0 and board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3]:
                return True
    # - diagonal win
    for i in range(0, 4):
        for j in range(3, 6):
            if board[i][j] != 0 and board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3]:
                return True
    # no wins were found
    return False


# player == 1 means player is red, player == 2 means player is yellow
def color(player):
    if player == 1:
        return red_color
    else:
        return yellow_color


# need to add failsafe for if column is full
def turn():
    global player, running
    waiting = True
    if waiting:
        if pygame.mouse.get_pressed():
            if not waiting:
                pass
            x, y = pygame.mouse.get_pos()
            count = 0
            for j in range(75, 875, 125):
                if not waiting:
                    pass
                if x >= j and x <= j + 100:
                    if not waiting:
                        pass
                    col = count
                    for i in range(6):
                        if board[col][i] == 0:
                            row = i
                            waiting = False
                count += 1
    try:
        dropPiece(player, col, row)
        if gameWon():
            textPrinting("Red won!", 500, 437.5, color(1))
            pygame.display.update()
            time.sleep(3)
            running = False
        player += 1
        pygame.draw.rect(screen, background_color, (0, 0, 1000, 50))
        textPrinting("Yellow Turn", 500, 25, color(2))
        pygame.display.update()
        time.sleep(.5)
        AITurn()
        if gameWon():
            textPrinting("Yellow won!", 500, 437.5, color(2))
            pygame.display.update()
            time.sleep(.5)
            running = False
        player -= 1
        pygame.draw.rect(screen, background_color, (0, 0, 1000, 50))
        textPrinting("Red Turn", 500, 25, color(1))
        pygame.display.update()
    except:
        pass

def scorePosition(board, player):
    score = 0
    # Score horizontal
    for r in range(6):
        row_array = [int(i) for i in list(board[:,r])]
        for c in range(4):
            window = row_array[c:c+4]
            if window.count(player) == 4:
                score += 100
            elif window.count(player) == 3:
                score += 10


def validColumns(board):
    potential_moves = []
    for col in range(7):
        found = False
        for i in range(6):
            if not found:
                if board[col][i] == 0:
                    potential_moves.append(col)
                    found = True

def bestMove(board, piece):
    pass


def AITurn():
    col = random.randint(0, 7)
    for i in range(6):
        if board[col][i] == 0:
            row = i
            waiting = False
    dropPiece(player, col, row)


def main():
    createIntBoard()
    gameSetup()


if __name__ == '__main__':
    main()
