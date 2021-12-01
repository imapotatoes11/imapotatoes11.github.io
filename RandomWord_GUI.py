import PySimpleGUI as sg
layout=[[sg.Button("Get")],
        [sg.Button("Close")]]
window=sg.Window("RandomWord Inquiry",layout,resizable=True)
event,values=window.read()
r=True
while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED or event=="Close":
        r=False
        window.close()
        break
    if event=="Get":
        import RandomWord
        with open("RandomWord.txt","r") as file:
            ja=file.read()
        window.close()
        break
if r:
    del layout,window,event,values
    layout=[
            [sg.Button("Close")],
            [sg.Text(ja)]
            ]
    window=sg.Window("RandomWord Result",layout,resizable=True)
    while True:
        event,values=window.read()
        if event==sg.WIN_CLOSED or event=="Close":
            break
window.close()