from microbit import *

#init game
display.scroll("Press A to start")
while not button_a.was_pressed():
    display.show(Image.ARROW_W)
    sleep(400)
    display.clear()
    sleep(400)

def gameWon(board):
    """
    returns a boolean that indicates if won or not
    """
    hasWon = True
    for i in range(2):
        for j in range(5):
            if board[i][j] == 9:
                hasWon = False
    return hasWon

def gameLost(ballPos):
    """
    returns a boolean that indicates if lost or not
    """
    return True if ballPos[0] == 4 else False

def updatePlayer(board, playerPos):
    """
    updates and returns the new board and position of player
    """
    if button_a.was_pressed() and playerPos != 0:
        board[4][playerPos - 1] = 8
        board[4][playerPos + 1] = 0
        playerPos -= 1
    elif button_b.was_pressed() and playerPos != 3:
        board[4][playerPos + 2] = 8
        board[4][playerPos] = 0
        playerPos += 1
    return board, playerPos

def updateBoard(board, ballPos):
    """
    updates the blocks/ball, moves the ball and returns the new board and ballPos
    """
    ballDirection = board[ballPos[0]][ballPos[1]]
    if ballDirection <= 2:
        #it's going up
        if ballPos[0] == 0: # check if at top
            board[ballPos[0]][ballPos[1]] += 2
        elif board[ballPos[0]-1][ballPos[1]] == 9: # check if block above
            board[ballPos[0]-1][ballPos[1]] = 0
            board[ballPos[0]][ballPos[1]] += 2
        elif ballDirection == 1 and ballPos[1] == 0: # check if at left wall
            board[ballPos[0]][ballPos[1]] += 1
        elif ballDirection == 2 and ballPos[1] == 4: # check if at right wall
            board[ballPos[0]][ballPos[1]] -= 1
        elif ballDirection == 1 and board[ballPos[0]][ballPos[1]-1] == 9: # check if block to left
            board[ballPos[0]][ballPos[1]-1] = 0
            board[ballPos[0]][ballPos[1]] += 1
        elif ballDirection == 2 and board[ballPos[0]][ballPos[1]+1] == 9: # check if block to right
            board[ballPos[0]][ballPos[1]+1] = 0
            board[ballPos[0]][ballPos[1]] -= 1
        elif ballDirection == 1 and board[ballPos[0]-1][ballPos[1]-1] == 9: # check if block left diagonal
            board[ballPos[0]-1][ballPos[1]-1] = 0
            board[ballPos[0]][ballPos[1]] = 4
        elif ballDirection == 2 and board[ballPos[0]-1][ballPos[1]+1] == 9: # check if block right diagonal
            board[ballPos[0]-1][ballPos[1]+1] = 0
            board[ballPos[0]][ballPos[1]] = 3
        #if no blocks obstructing:
        elif ballDirection == 1:
            #move in direction
            board[ballPos[0]-1][ballPos[1]-1] = ballDirection
            board[ballPos[0]][ballPos[1]] = 0
            ballPos[0] -= 1
            ballPos[1] -= 1
        elif ballDirection == 2:
            #move in direction
            board[ballPos[0]-1][ballPos[1]+1] = ballDirection
            board[ballPos[0]][ballPos[1]] = 0
            ballPos[0] -= 1
            ballPos[1] += 1
    else:
        #it's going down
        if board[ballPos[0]+1][ballPos[1]] == 8: # check if player below
            board[ballPos[0]][ballPos[1]] -= 2
        elif board[ballPos[0]+1][ballPos[1]] == 9: # check if block below
            board[ballPos[0]][ballPos[1]] -= 2
            board[ballPos[0]+1][ballPos[1]] = 0
        elif ballDirection == 3 and ballPos[1] == 0: # check if at left wall
            board[ballPos[0]][ballPos[1]] += 1
        elif ballDirection == 4 and ballPos[1] == 4: # check if at right wall
            board[ballPos[0]][ballPos[1]] -= 1
        elif ballDirection == 3 and board[ballPos[0]+1][ballPos[1]-1] == 8: # check if player left diagonal
            board[ballPos[0]][ballPos[1]] = 2
        elif ballDirection == 4 and board[ballPos[0]+1][ballPos[1]+1] == 8: # check if player right diagonal
            board[ballPos[0]][ballPos[1]] = 1
        elif ballDirection == 3 and board[ballPos[0]][ballPos[1]-1] == 9: # check if block to left
            board[ballPos[0]][ballPos[1]-1] = 0
            board[ballPos[0]][ballPos[1]] += 1
        elif ballDirection == 4 and board[ballPos[0]][ballPos[1]+1] == 9: # check if block to right
            board[ballPos[0]][ballPos[1]+1] = 0
            board[ballPos[0]][ballPos[1]] -= 1
        elif ballDirection == 3 and board[ballPos[0]+1][ballPos[1]-1] == 9: # check if block left diagonal
            board[ballPos[0]][ballPos[1]] = 2
            board[ballPos[0]+1][ballPos[1]-1] = 0
        elif ballDirection == 4 and board[ballPos[0]+1][ballPos[1]+1] == 9: # check if block right diagonal
            board[ballPos[0]][ballPos[1]] = 1
            board[ballPos[0]+1][ballPos[1]+1] = 0
        #if no obstructions
        elif ballDirection == 3:
            #move in direction
            board[ballPos[0]+1][ballPos[1]-1] = ballDirection
            board[ballPos[0]][ballPos[1]] = 0
            ballPos[0] += 1
            ballPos[1] -= 1
        elif ballDirection == 4:
            #move in direction
            board[ballPos[0]+1][ballPos[1]+1] = ballDirection
            board[ballPos[0]][ballPos[1]] = 0
            ballPos[0] += 1
            ballPos[1] += 1
    return board, ballPos

def updateLED(board):
    """
    sets the LED ''pixels' according to the board
    """
    for i in range(len(board)): # it will be 5x5, but may as well assign dynamically
        for j in range(len(board[0])):
            if board[i][j] > 0:
                display.set_pixel(j, i, 9)
            else:
                display.set_pixel(j, i, 0)

display.scroll("Breakout...")

board = [
        [9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9],
        [0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0],
        [8, 8, 0, 0, 0],
        ]
ballPos = [3, 1]
playerPos = 0 # along the bottom row
updateLED(board)

while not gameWon(board) and not gameLost(ballPos):
    for i in range(4):
        board, playerPos = updatePlayer(board, playerPos)
        updateLED(board)
        sleep(125)
    board, playerPos = updatePlayer(board, playerPos)
    board, ballPos = updateBoard(board, ballPos)
    updateLED(board)
    sleep(50)

if gameLost(ballPos):
    display.scroll("You lose!")
    display.show(Image.SAD)
else:
    display.scroll("You win!")
    display.show(Image.HAPPY)


