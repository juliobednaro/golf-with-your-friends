import mouse
import time
from pynput.keyboard import Key, Controller
import pyautogui
import pydirectinput as pg
import win32api
import win32con

i = 0
while i < 6000:
    time.sleep(4)
    pg.mouseDown()
    x, y = mouse.get_position()
    pg.moveRel(0, -1)
    pg.mouseUp()
    i += 1
    print("Proba", i)
