"""import pyautogui as py
from pynput.mouse import Button,Controller
mouse=Controller()
import sys
sys.platform = '_'

while True:
 pos=mouse.position
 print(pos)
 im=py.screenshot()
 px=im.getpixel((pos))
 print(px)"""
import time
from PIL import ImageGrab
import PIL.ImageGrab
from pynput.mouse import Button,Controller
mouse=Controller()

e=list(mouse.position)
print("MOVE MOUSE AWAY")
time.sleep(2.5)
image = ImageGrab.grab()
print(e)
e[0]=e[0]-10
e[1]=e[1]-10
print(e)
color = image.getpixel(tuple(e))
print(color)