
import logging,time,random,sys

from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard=KeyboardController()
mouse=MouseController()
print("starting...")
time.sleep(10)
def spmclick():
    for jj in range(5):
        mouse.press(Button.right)
        mouse.release(Button.right)
        time.sleep(0.0001)
for i in range(10):
    mouse.press(Button.left)

    mouse.press(Button.right)
    mouse.release(Button.right)
    time.sleep(0.0001)

    keyboard.press(Key.shift)

    mouse.press(Button.right)
    mouse.release(Button.right)
    time.sleep(0.0001)

    keyboard.press("s")

    mouse.press(Button.right)
    mouse.release(Button.right)
    time.sleep(0.0001)

    time.sleep(0.5)

    mouse.press(Button.right)
    mouse.release(Button.right)
    time.sleep(0.0001)

    keyboard.release(Key.shift)

    mouse.press(Button.right)
    mouse.release(Button.right)
    time.sleep(0.0001)

keyboard.release("s")