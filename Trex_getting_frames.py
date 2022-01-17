# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 23:41:06 2021

@author: Efe Kurdoğlu
"""

"""

http://www.trex-game.skipser.com/

"""

import keyboard 
import uuid
import time
from PIL import Image
from mss import mss

# =============================================================================
# you may need to install library of keyboard and mss by 'pip install mss' or 'pip install keyboard'
# =============================================================================
mon = {"top":385, "left":520, "width":250, "height":100} 
# =============================================================================
# you should change the coordinates according to your screen
# =============================================================================

sct = mss() 
# =============================================================================
# This helps us to convert ROC of mon into frame
# =============================================================================

i = 0

def frames(id, key): # key is the buttons from the keyboard
    global i
    
    i += 1
    print("{}: {}".format(key, i)) # key: up, down, left, right arrow
                                    # i: for how many times we pressed the button
    img = sct.grab(mon) # get the ROC with the size of specified in mon
    im = Image.frombytes("RGB", img.size, img.rgb)
    im.save("./images/{}_{}_{}.png".format(key, id, i))
    
is_exit = False

def exit():
    global is_exit
    is_exit = True
    
keyboard.add_hotkey("esc", exit)
id = uuid.uuid4()

while True:
    
    if is_exit: break

    try: 
        if keyboard.is_pressed(keyboard.KEY_UP):
            frames(id, "up")
            time.sleep(0.1)
        elif keyboard.is_pressed(keyboard.KEY_DOWN):
            frames(id, "down")
            time.sleep(0.1)
        elif keyboard.is_pressed("right"):
            frames(id, "right")
            time.sleep(0.1)
    except RuntimeError: continue


"""
    Defining two buttons "up" and "down" seems to be enough but now exactly. 
We need to have data as much as we can 
so that "right" command has been added not to mix up "up" and "down".

"""
























































