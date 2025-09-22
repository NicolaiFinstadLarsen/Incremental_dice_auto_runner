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
    # Just big now to not use up all the upgrades in testing. 
    time_to_upgrade = 0

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
            go_to_shop_tab(False)
        upgrade_counter += 1

        # Move back to top. 
        pyag.moveTo(full_right_x, top_y, duration=0)


def go_to_shop_tab(been_in_upgrade):
    # Shop tab button Point(x=4155, y=105)
    pydi.moveTo(4155, 105)
    time.sleep(1)
    pydi.mouseDown()
    time.sleep(1)
    pydi.mouseUp()
    if been_in_upgrade == True:
        play_game()
    else:
        check_shop_tab()


def check_shop_tab():
    # Checking if pixel for fist upgrade is green
    # 1st upgrade pos = middle: Point(x=4397, y=216) bottom:(x=4398, y=224)
    # Middle of first upgrade button ish(x=4276, y=207)
    if pyag.pixelMatchesColor(4397, 216, (0,255,0)) or pyag.pixelMatchesColor(4398, 224, (0, 255, 0)):
        pydi.moveTo(4276, 207)
        time.sleep(1)
        pydi.mouseDown()
        time.sleep(1)
        pydi.mouseUp()
        # Move back to start pos.
        pydi.moveTo(2617, 26, duration=0)
        play_game()

    #Check upgrade nr 2
    # 2nd upgrade pos = middle: Point(x=4399, y=321) bottom:(x=4398, y=327)
    # Middle button Point(x=4297, y=300
    elif pyag.pixelMatchesColor(4399, 321, (0,255,0)) or pyag.pixelMatchesColor(4398, 327, (0, 255, 0)):
        pydi.moveTo(4297, 300)
        time.sleep(1)
        pydi.mouseDown()
        time.sleep(1)
        pydi.mouseUp()
        # Move back to start pos.
        pydi.moveTo(2617, 26, duration=0)
        play_game()
    else:
        go_to_upgrade_tab()

    play_game()

    '''
    TODO
    Check for more upgrades.
    '''


def go_to_upgrade_tab():
    # Upgrade tab pos Point(x=4356, y=107)
    pydi.moveTo(4356, 107)
    time.sleep(1)
    pydi.mouseDown()
    time.sleep(1)
    pydi.mouseUp()
    check_shop_upgrade_tab()


def check_shop_upgrade_tab():
    # Same pos as shop tab
    # Check for green pixel in price
    if pyag.pixelMatchesColor(4397, 216, (0,255,0)) or pyag.pixelMatchesColor(4398, 224, (0, 255, 0)):
        pydi.moveTo(4276, 207)
        time.sleep(1)
        pydi.mouseDown()
        time.sleep(1)
        pydi.mouseUp()
        # Value 1 to play game in func
        go_to_shop_tab(True)

    elif pyag.pixelMatchesColor(4399, 321, (0,255,0)) or pyag.pixelMatchesColor(4398, 327, (0, 255, 0)):
        pydi.moveTo(4297, 300)
        time.sleep(1)
        pydi.mouseDown()
        time.sleep(1)
        pydi.mouseUp()
        # Value 1 to play game in func
        go_to_shop_tab(True)

    go_to_shop_tab(True)


def skill_tree():
    pass
    '''
    TODO
    Is it possible to do somthing in skill tree?
    '''

play_game()
