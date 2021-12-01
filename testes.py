import logging,time,random,sys

from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
mouse=MouseController()
keyboard=KeyboardController()
time.sleep(5)
for i in range(5):
    keyboard.press("s")
    time.sleep(1)
    keyboard.release("s")