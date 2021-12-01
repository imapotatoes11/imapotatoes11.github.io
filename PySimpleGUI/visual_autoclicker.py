import PySimpleGUI as sg
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import os
import sys

# ---------------------------------------------------------------------------------------
# GUI STUFF
sg.theme('LightGrey2')
# All the stuff inside your window.
layout = [[sg.Text('Left Mouse Clicker in Python using PySimpleGUI and Pynput')],
          [sg.Text('Toggle clicking (shortcut)'), sg.InputText(), sg.Button('Enter')],
          [sg.Button('Close'), sg.Button('Exit')]]

# -----------------------------------------------------------------------------------------------
# autoclicker functions and threading functions and stuff idk copied it from "C:\Users\Wzm82\PycharmProjects\click\autoclickerv3.py"
# from line like 14 to line like 52

# Create the Window
window = sg.Window('Test', layout)
event, values = window.read()

delay = 0.001
button = Button.left
start_stop_key = KeyCode(char=values[0])
exit_key = KeyCode(char='e')


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


# ----------------------------------------------------------------------
# GUI/BUTTON SETUP

count = 0
while True:
    count += 1
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit' or event == 'Close':  # if user closes window or clicks cancel
        break
    if event == 'Enter':
        start_stop_key = KeyCode(char=values[0])
        print(start_stop_key)
        temp = values[0]
        window.close()
        time.sleep(0.1)
        layout2 = [[sg.Text('Left Mouse Clicker in Python using PySimpleGUI and Pynput')],
                   [sg.Text('Toggle clicking (shortcut)'), sg.InputText(start_stop_key), sg.Button('Quit')],
                   [sg.Button('Close'), sg.Button('Exit')]] 

        print("Shortcut: " + temp)
    if count >= 1000:
        break
    with Listener(on_press=on_press) as listener:
        layout2.append([sg.Text('Shortcut key: ' + str(start_stop_key))])
        layout2.append([sg.Text('(Reopen to Rebind Shortcut')])
        window2 = sg.Window('Test2', layout2)
        event1, values1 = window2.read()
        listener.join()
    if event1 == 'Close' or event1 == 'Exit':
        break
    if event1 == "Quit":
        break
        # os.system("python visual_autoclicker.py")
        # os.execv(__file__, sys.argv)
window.close()
