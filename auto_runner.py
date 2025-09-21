import pyautogui as pyag
import pydirectinput as pydi
import time

# Move to top left second screen
pyag.moveTo(2617, 26, duration=0)

'''
Top right in game: x=4073, y=26
Bottom left in game: x=4073, y=26
Bottom right in game: x=4073, y=1034
'''

# All varible inputs are made for the game to run before any upgrades.
# Can be changed after upgrades have been purchased for faster gameplay.
def play_game():
    # Game screen pos on 2nd monitor
    full_right_x = 4073
    top_y = 26
    bottom_y = 1034
    full_left_x = 2617

    # How far the mouse moves down
    pixel_movement = 20 # Slow but hits all at no area increase

    # The duration the mouse uses from start to stop pos
    speed = 1.75 # Seems to pick up dice with no faster speed that this

    # Checking for upgrade every so often
    upgrade_counter = 0
    time_to_upgrade = 3

    while True:
        change_y = top_y

        while change_y < bottom_y:
            pyag.moveTo(full_right_x, change_y, duration = speed)
            change_y = change_y + pixel_movement
            pyag.moveTo(full_left_x, change_y, duration=speed)
            change_y = change_y + pixel_movement

            time.sleep(0.1) # Recommended for doc's

        # Checking upgrade after x full screen crawls.
        if upgrade_counter == time_to_upgrade:
            check_upgrade()
        upgrade_counter += 1

        # Move back to top. 
        pyag.moveTo(full_right_x, top_y, duration=0)

def check_upgrade():
    # Pixel for first upgrade: x=4400, y=212
    # Middle of first upgrade button ish(x=4276, y=207)
    
    # Checking if pixel for fist upgrade is green
    if pyag.pixelMatchesColor(4400, 212, (0,255,0)):
        pydi.moveTo(4276, 207)
        time.sleep(1)
        pydi.mouseDown()
        time.sleep(1)
        pydi.mouseUp()
        # Move back to start pos.
        pydi.moveTo(2617, 26, duration=0)
        play_game()

    #Check upgrade nr 2
    # 2nd upgrade pos = Point(x=4365, y=321)
    # Middle button Point(x=4297, y=300
    elif pyag.pixelMatchesColor(4365, 321, (0,255,0)):
        pydi.moveTo(4297, 300)
        time.sleep(1)
        pydi.mouseDown()
        time.sleep(1)
        pydi.mouseUp()
        # Move back to start pos.
        pydi.moveTo(2617, 26, duration=0)
        play_game()
    

    play_game()

play_game()
