from microbit import *

#init game
display.scroll("Press A to start")
while not button_a.was_pressed():
    display.show(Image.ARROW_W)
    sleep(400)
    display.clear()
    sleep(400)

display.scroll("Breakout...")

board = [
        [9, 9, 9, 9, 9]
        [9, 9, 9, 9, 9]
        [0, 0, 0, 0, 0]
        [0, 1, 0, 0, 0]
        [9, 9, 0, 0, 0]
        ]
ballPos = [3, 1]
playerPos = 0 # along the bottom row

while not gameWon() and not gameLost():
    for i in range(4):
        updatePlayer()
        sleep(250)
    updatePlayer()
    updateBoard()

def gameWon():
    hasWon = True
    for i in range(2):
        for j in range(5):
            if board[i][j] == 9:
                hasWon = False
    return hasWon

def gameLost():
    #TODO
    pass

def updatePlayer():
    #TODO
    pass

def updateBoard():
    #TODO
    pass
