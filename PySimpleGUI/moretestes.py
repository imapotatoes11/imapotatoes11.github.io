import PySimpleGUI as sg
layout=[[sg.Text("Input: "),sg.InputText()]]
window=sg.Window("Poutput",layout)
sg.main()
while True:
    event,values=window.read()
    secs=str(values[0])
    if secs!="" or secs!=" ":
        print("EEEEEEEE")
    if event==sg.WIN_CLOSED:
        break