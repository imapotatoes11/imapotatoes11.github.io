import os
import PySimpleGUI as sg
import random as random
import time as t

"web browser stuff"
import webbrowser
chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
import subprocess
"web browser stuff"

sg.theme('LightGrey2')
layout=[[sg.Text('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')],
        [sg.Button('Click me')],
        [sg.Button('Exit')]]
window=sg.Window('RWA', layout)
while True:
    event, values=window.read()
    if event=='Click me':
        #os.system(subprocess.call(list(chrome_path)))
        subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe'])
        t.sleep(0.5)
        webbrowser.open('https://en.wikipedia.org/wiki/Special:Random')
        t.sleep(0.2)
        for i in range(4):
            webbrowser.open_new_tab('https://en.wikipedia.org/wiki/Special:Random')
            t.sleep(0.2)
        webbrowser.open_new_tab('https://www.news.google.com')
        t.sleep(0.2)
        webbrowser.open_new_tab('https://www.theweathernetwork.com/ca/hourly-weather-forecast/ontario/toronto')
        t.sleep(0.2)
        webbrowser.open_new_tab('https://www.google.com/search?q=weather&oq=weather')
    if event=='Exit' or event==sg.WIN_CLOSED:
        window.close()
        break
