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
        [0, 9, 0, 0, 0]
        [9, 9, 0, 0, 0]
        ]
