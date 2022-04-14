"""
- After manually spawning:

- full speed for 46s

- press T to reverse

- wait for 4s

- press T to load passengers

- wait for 33s

- full speed for 4:25m

- press T to load

- wait for 33s

- full speed for 2:43m

- press T to load

- wait for 33s

- full speed for 3:30m

- press T to unload

- wait for 33s

- You completed your trip! Reverse:

- click at Point(x=854, y=579) to reverse

- wait for 4s

- press T to load

- wait 33s

- full speed for 3:30m

- press T to load

- wait 33s

- full speed for 2:43m

- press T to load

- wait 33s

- full speed for 4:25

- press T to unload

- wait for 33s

- click at Point(x=854, y=579) to reverse

- jump to line 8 (wait for 4s)

- takes 45 seconds to go full speed (65 km/h or something)
- if you stop from 300m to destination, it takes 24s to stop
- takes 1:43 to travel 1.2km (~0.84km/h)
- the left button to redo route is at 
- wait 4s after pressing redo route button
"""

import pyautogui
import time

but_x, but_y = 854, 579 # x, y screen coordinates of the reverse button

def full_speed(t):
    """ 
    throttle up and release breaks
    wait for t seconds
    throttle down and use breaks
    wait 26s to slow down 
    """
    pyautogui.hotkey('w','a', interval=3)
    time.sleep(t)
    pyautogui.hotkey('s','d', interval=3)
    time.sleep(26)

def T():
    # press T to load, reverse, or unload
    pyautogui.press('t')

def wait(t):
    time.sleep(t)

wait(5) # wait 5 seconds before starting
full_speed(46)
T()

while True:
    # Zand - Hazel
    wait(4)
    T()
    wait(33)
    full_speed(265)
    T()
    wait(33)
    full_speed(163)
    T()
    wait(33)
    full_speed(210)
    T()
    wait(33)
    
    # Hazel - Zand
    pyautogui.click(x=but_x, y=but_y)
    wait(4)
    T()
    wait(33)
    full_speed(210)
    T()
    wait(33)
    full_speed(163)
    T()
    wait(33)
    full_speed(265)
    T()
    wait(33)
    pyautogui.click(x=but_x, y=but_y)