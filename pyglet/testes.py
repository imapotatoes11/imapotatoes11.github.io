import time

import pyglet
from pyglet.window import key
import PySimpleGUI as sg

#effectively a python keylogger (as long as the typing happens while the python window is active

window = pyglet.window.Window()
label = pyglet.text.Label('Type on this window!',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
@window.event
def on_draw():
    window.clear()
    label.draw()
keys=[]
@window.event
def on_key_press(symbol,modifiers):
    labele = pyglet.text.Label("null", font_name='Times New Roman', font_size=20, x=window.width // 2,
                               y=window.height // 2, anchor_x='center')
    with open("testes.txt","w") as r:
        r.write(" ")
    global keys
    if symbol==key.A:
        print("A was pressed")
        keys.append("a")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.B:
        print("B was pressed")
        keys.append("b")

        layout = [[sg.Text(keys)]]
        windowe = sg.Window("Textes", layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout, windowe,event,values

    elif symbol==key.C:
        print("C was pressed")
        keys.append("c")

        layout = [[sg.Text(keys)]]
        windowe = sg.Window("Textes", layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout, windowe,event,values

    elif symbol==key.D:
        print("D was pressed")
        keys.append("d")

        layout = [[sg.Text(keys)]]
        windowe = sg.Window("Textes", layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout, windowe,event,values

    elif symbol==key.E:
        print("E was pressed")
        keys.append("e")

        layout = [[sg.Text(keys)]]
        windowe = sg.Window("Textes", layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout, windowe,event,values

    elif symbol==key.F:
        print("F was pressed")
        keys.append("f")

        layout = [[sg.Text(keys)]]
        windowe = sg.Window("Textes", layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout, windowe,event,values

    elif symbol==key.G:
        print("G was pressed")
        keys.append("g")

        layout = [[sg.Text(keys)]]
        windowe = sg.Window("Textes", layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout, windowe,event,values

    elif symbol==key.H:
        print("H was pressed")
        keys.append("h")

        layout = [[sg.Text(keys)]]
        windowe = sg.Window("Textes", layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout, windowe,event,values

    elif symbol==key.I:
        print("I was pressed")
        keys.append("i")

        layout = [[sg.Text(keys)]]
        windowe = sg.Window("Textes", layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout, windowe,event,values

    elif symbol==key.J:
        print("J was pressed")
        keys.append("j")

        layout = [[sg.Text(keys)]]
        windowe = sg.Window("Textes", layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout, windowe,event,values

    elif symbol==key.K:
        print("K was pressed")
        keys.append("k")

        layout = [[sg.Text(keys)]]
        windowe = sg.Window("Textes", layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout, windowe,event,values

    elif symbol==key.L:
        print("L was pressed")
        keys.append("l")

        layout = [[sg.Text(keys)]]
        windowe = sg.Window("Textes", layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout, windowe,event,values

    elif symbol==key.M:
        print("M was pressed")
        keys.append("m")

        layout = [[sg.Text(keys)]]
        windowe = sg.Window("Textes", layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout, windowe,event,values

    elif symbol==key.N:
        print("N was pressed")
        keys.append("n")

        layout = [[sg.Text(keys)]]
        windowe = sg.Window("Textes", layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout, windowe,event,values

    elif symbol==key.O:
        print("O (letter) was pressed")
        keys.append("o")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.P:
        print("P was pressed")
        keys.append("p")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.Q:
        print("Q was pressed")
        keys.append("q")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.R:
        print("R was pressed")
        keys.append("r")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.S:
        print("S was pressed")
        keys.append("s")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.T:
        print("T was pressed")
        keys.append("t")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.U:
        print("U was pressed")
        keys.append("u")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.V:
        print("V was pressed")
        keys.append("v")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.W:
        print("W was pressed")
        keys.append("w")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.X:
        print("X was pressed")
        keys.append("x")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.Y:
        print("Y was pressed")
        keys.append("y")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.Z:
        print("Z was pressed")
        keys.append("z")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.NUM_0:
        print("0 was pressed")
        keys.append("0")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.NUM_1:
        print("1 was pressed")
        keys.append("1")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.NUM_2:
        print("2 was pressed")
        keys.append("2")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.NUM_3:
        print("3 was pressed")
        keys.append("3")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.NUM_4:
        print("4 was pressed")
        keys.append("4")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.NUM_5:
        print("5 was pressed")
        keys.append("5")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.NUM_6:
        print("6 was pressed")
        keys.append("6")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.NUM_7:
        print("7 was pressed")
        keys.append("7")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.NUM_8:
        print("8 was pressed")
        keys.append("8")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.NUM_9:
        print("9 was pressed")
        keys.append("9")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.SPACE:
        print("SPACEBAR was pressed")
        keys.append(" ")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.ENTER:
        print("ENTER was pressed")
        keys.append("\n")

        layout=[[sg.Text(keys)]]
        windowe=sg.Window("Textes",layout)
        event,values=windowe.read()
        time.sleep(0.5)
        windowe.close()
        del layout,windowe,event,values

    elif symbol==key.BACKSPACE:
        print("BACKSPACE was pressed")
    elif symbol==key.BACKSLASH:
        print("Entering Debug Mode...")
        layout=[[sg.Text("Proceed to Debug Mode?")],
                [sg.Button("Proceed")]]
        windowe=sg.Window("Debug Mode",layout)
        while True:
            event,values=windowe.read()
            if event==sg.WIN_CLOSED or event=="Proceed":

                break
        windowe.close()
        del layout,windowe,event,values
        print("Redirecting...")
        time.sleep(1)
        from GUI.PySimpleGUI.websites_loginsystem_function import do
        do.Do("e")
        import GUI.PySimpleGUI.websites
    else:
        print("An unidentified key was pressed")
    window.clear()
    labele.draw()


pyglet.app.run()
print("".join(keys))