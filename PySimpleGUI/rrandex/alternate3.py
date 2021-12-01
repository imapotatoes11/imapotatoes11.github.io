import PySimpleGUI as sg
sg.theme('LightGrey2')
layout=[[sg.Text('EEEeeEeEeeeeEEEEeee!!!')],
        [sg.Button('Close')]]
window=sg.Window('rrandex result',layout)
while True:
    event,values=window.read()
    if event=='Close' or event==sg.WIN_CLOSED:
        break
window.close()