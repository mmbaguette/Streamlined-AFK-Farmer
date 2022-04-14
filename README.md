﻿# Streamlined Farmer

A Python script that controls your keypresses in the Roblox train simulator [Streamlined](https://www.roblox.com/games/1788251222/) so that you can farm for Gulden and levels. This was specifically made and timed for the NS 4500 train from  with seven third class C8c wagons, so it's completely beginner friendly!

![image](https://user-images.githubusercontent.com/76597978/163438984-e2c9e77d-8f47-45a4-956a-7f999e18dbd7.png)

### Prerequisites:

Python 3: https://www.python.org/

Once you've [added the Python executable](https://www.geeksforgeeks.org/how-to-add-python-to-windows-path/) to your PATH variable (this is the hard part), open a command prompt or Powershell and enter this command to install the `pyautogui` library needed for keypresses.
```
pip install pyautogui
```
If you're not using Windows 10 or are having trouble installing, see https://pyautogui.readthedocs.io/en/latest/install.html.

Download the [main.py](main.py) script, and edit the variables `but_x` and `but_y` which determine the X and Y coordinates of the "Reverse" button that pops up after completing a trip.

If you want to use a **different train with different carts, and a different route**, then change the time values (in seconds) inside the Python script, or copy some lines around and make your own! 

Once you're setup, just spawn your train and the carts using a specific route. Run the script using Python, or use the command `python main.py` (may be different on Mac or Linux), and go back to Roblox as fast as possible, because the script will start running in 5 seconds! 

Happy farming!

**NOTE:** This project was not made to harm any of the developers, and was simply created for fun. 
