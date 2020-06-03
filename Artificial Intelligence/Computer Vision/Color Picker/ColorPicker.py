import pyautogui as pg
import numpy as numpy

while True:
    x_pos, y_pos = pg.position()
    new_shot = pg.screenshot()
    print(new_shot.getpixel((x_pos, y_pos)))

# If left clicked then fix the changing of pixel value 
# copy that pixel value
# if right clicked then restart the loop and color will change
# Show the color code in rgb and also in hex