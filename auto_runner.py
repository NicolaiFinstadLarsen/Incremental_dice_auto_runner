import pyautogui as pyg
import time

print(pyg.position())

#Move to top left second screen
pyg.moveTo(2617, 26, duration=0)

# Top right in game: x=4073, y=26
# Bottom left in game: x=4073, y=26
# Bottom right in game: x=4073, y=1034

def play_game():
    full_right_x = 4073
    top_y = 26
    bottom_y = 1034
    full_left_x = 2617

    pixel_movement = 30

    while True:
        change_y = top_y

        while change_y < bottom_y:
            pyg.moveTo(full_right_x, change_y, duration=1)
            change_y = change_y + pixel_movement
            pyg.moveTo(full_left_x, change_y, duration=0)

            time.sleep(0.1) # Recommended for doc's
        
        pyg.moveTo(full_right_x, top_y, duration=0)

play_game()
