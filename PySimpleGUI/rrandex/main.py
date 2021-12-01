import PySimpleGUI as sg
import sys
sg.theme('LightGrey2')
layout=[[sg.Text('rrandex')],
        [sg.Button('0')],
        [sg.Button('1')],
        [sg.Button('2')],
        [sg.Button('3')],
        [sg.Button('4')],
        [sg.Button('5')],
        [sg.Button('6')],
        [sg.Button('7')],
        [sg.Button('8')],
        [sg.Button('9')],
        [sg.Button('Close')]]
window=sg.Window('rrandex',layout)
result=[]
success=False
alternate1=False
while True:
    event,values=window.read()
    if event=='Close' or event==sg.WIN_CLOSED:
        break
    if event=='0':
        result.append(0)
        print(0)
    if event=='1':
        result.append(1)
        print(1)
    if event=='2':
        result.append(2)
        print(2)
    if event=='3':
        result.append(3)
        print(3)
    if event=='4':
        result.append(4)
        print(4)
    if event=='5':
        result.append(5)
        print(5)
    if event=='6':
        result.append(6)
        print(6)
    if event=='7':
        result.append(7)
        print(7)
    if event=='8':
        result.append(8)
        print(8)
    if event=='9':
        result.append(9)
        print(9)
    if result==[1,2,3,4,5]:
        success=True
        break
    if result==[0,8,2,5]:
        alternate1=True
        break 
window.close()
if alternate1:
    import alternate1.py
if success:
    del layout,event,values,window
    layout=[[sg.InputText(r'C:\Users\wzm82\AppData\Local\pip\cache\wheels\88\cc\ea\9d254284e8987d83b1693e527caa0494ac72e9845b42b22ccc')],
            [sg.Button('Close'),sg.Button('Reopen')]]
    window=sg.Window('rrandex',layout)
    while True:
        event,values=window.read()
        if event=='Close' or event==sg.WIN_CLOSED:
            break
        if event=='Reopen':
            window.close() 
            print('Success!')
            import main.py
    window.close()
    print('Success!')