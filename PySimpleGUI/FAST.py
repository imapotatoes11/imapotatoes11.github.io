import PySimpleGUI as sg
ticks=0
while True:
    layout=[[sg.Text(str(ticks)+"Ticks past")]]
    window=sg.Window("F.A.S.T.",layout)
    window.close()
    del layout, window
    ticks+=1