import PySimpleGUI as sg
sg.theme('LightGrey2')
layout=[[sg.Text('00o0o0ooo0o0000o0oo0oooo0o0oo00ooo!!!')],
        [sg.Button('Close')]]
window=sg.Window('rrandex result',layout)
while True:
    event,values=window.read()
    if event=='Close' or event==sg.WIN_CLOSED:
        break
window.close()