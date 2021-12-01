#import PySimpleGUI as sg
from pynput.mouse import Button, Controller, Listener
#from pynput.keyboard import Listener
import logging, time, random, sys

mouse = Controller()


class click:
    def toggleclick(value=True):
        pos = mouse.position
        global start
        start = time.time()
        global failsafestart
        failsafestart = time.time()

        startt = input("Start? ")
        if startt == "stop":
            sys.exit()
        pos = mouse.position
        print(pos)
        time.sleep(0.5)
        #ji = int(input("Number of Clicks: ")) - 1
        conf = startt
        ji = random.randint(1000,2000)
        ji=int(input("Number of Clicks: "))-1
        if conf == "stop":
            sys.exit()
        time.sleep(0.35)
        print("Starting...")
        time.sleep(1)
        counter = 0
        pos = mouse.position
        while counter <= ji:
            mouse.press(Button.left)
            mouse.release(Button.left)
            ss = random.randrange(0, 10, 10) / 100
            print("delay " + str(ss))
            time.sleep(ss)
            counter = counter + 1
            print("counter: " + str(counter))
            poss = mouse.position
            if poss != pos:
                print("Exited")
                sys.exit()


while True:
    click.toggleclick(True)
    global end, failsafeend
    end = time.time()
    failsafeend = time.time()
    if failsafeend - failsafestart >= 7:
        break
    print("Program finished at " + str(round(end - start, 2)) + " seconds elapsed.")
