import PySimpleGUI as sg
sg.theme('LightGrey2')
while True:
    layout=[[sg.Button('Click me!')]]
    window=sg.Window(layout)
    while True:
        event, values=window.read()
        if event==sg.WIN_CLOSED or event=='Click me!':
            window.close()
            break
    del window
    del layout