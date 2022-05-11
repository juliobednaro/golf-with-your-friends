import time
from pynput.keyboard import Key, Controller
import pydirectinput as pg

keyboard = Controller()
key = Key.esc
# pyautogui.mouseInfo()

while True:
    time.sleep(5)
    keyboard.press(key)
    keyboard.release(key)
    time.sleep(0.5)
    pg.moveTo(280, 620)
    pg.click()
    print("forfeited a hole")
