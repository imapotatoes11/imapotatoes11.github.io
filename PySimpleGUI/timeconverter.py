import PySimpleGUI as sg
def digital_clock(seconds):
    hours=(seconds//60)//60
    minutes=(seconds//60)%60
    secs=seconds%60
    return str(hours)+':'+str(minutes)+':'+str(secs)
sg.theme('LightGrey2')
layout = [[sg.Text('Convert Seconds to HH:MM:SS')],
          [sg.InputText()],
          [sg.Button('Enter'),sg.Button('Close')]]
window=sg.Window('HELLO',layout,resizable=True,finalize=True)
event,values=window.read()
while True:
    event,values=window.read()
    if event=='Enter':
        secs=values[0]
        print('Entered: ',secs)
        window.close()
        del layout, event, values, window
        layout = [[sg.Text('Result (HH:MM:SS): '+str(digital_clock(int(secs))))],
                  [sg.Button('Close')]]
        window = sg.Window('Result', layout,resizable=True,finalize=True)
        event, values = window.read()
        while True:
            event,values=window.read()
            if event=='Close' or event==sg.WIN_CLOSED:
                window.close()
                break

    if event==sg.WIN_CLOSED or event=='Close':
        window.close()
        break
window.close()