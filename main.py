"""
- takes 45 seconds to go full speed (65 km/h or something)
- if you stop from 300m to destination, it takes 24s to stop
- takes 1:43 to travel 1.2km (~0.84km/h)
- the left button to redo route is at 
- wait 4s after pressing redo route button
"""

import pydirectinput
import time

def full_speed(t):
    """ 
    throttle up and release breaks
    wait for t seconds
    throttle down and use breaks
    wait 26s to slow down 
    """
    pydirectinput.keyDown('w')
    pydirectinput.keyDown('a')
    time.sleep(3)
    pydirectinput.keyUp('w')
    pydirectinput.keyUp('a')
    time.sleep(t)
    pydirectinput.keyDown('s')
    pydirectinput.keyDown('d')
    time.sleep(3)
    pydirectinput.keyUp('s')
    pydirectinput.keyUp('d')
    time.sleep(26)

def T():
    # press T to load, reverse, or unload
    pydirectinput.press('t')

def wait(t):
    time.sleep(t)

print("Welcome to MmBaguette's train farmer!")
wait(5) # wait 5 seconds before starting
print("On my way to the first station!")
full_speed(43)
T()
print("I just reversed the train!")

while True:
    # Zand - Hazel
    print("Let's go from Zand op 't Zee to Hazeldrecht!")
    wait(5)
    T()
    wait(33)
    full_speed(263)
    print("Welcome to the second station!")
    T()
    wait(33)
    full_speed(161)
    print("Welcome to the third station!")
    T()
    wait(33)
    full_speed(207)
    print("We've arrived at Hazeldrecht!")
    T()
    print("Unloading passengers...")
    wait(45)

    # Hazel - Zand
    print("Let's go from Hazeldrecht to Zand op 't Zee!")
    input("Click the reverse button, then come back here and press [Enter] to continue.")
    wait(5)
    print("Loading our first passengers...")
    T()
    wait(33)
    full_speed(207)
    print("Welcome to the second station!")
    T()
    wait(33)
    full_speed(161)
    print("Third station!")
    T()
    wait(33)
    full_speed(263)
    print("We're back at Zand op 't Zee!")
    T()
    wait(33)
    print("Click the reverse button, then come back here and press [Enter] to continue.")