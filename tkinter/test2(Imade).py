from tkinter import *
import tkinter as tk

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
root = Tk()

class RoundedButton(tk.Canvas):
    def __init__(self, parent, width, height, cornerradius, padding, color, bg, command=None):
        tk.Canvas.__init__(self, parent, borderwidth=0,
            relief="flat", highlightthickness=0, bg=bg)
        self.command = command

        if cornerradius > 0.5*width:
            print("Error: cornerradius is greater than width.")
            return None

        if cornerradius > 0.5*height:
            print("Error: cornerradius is greater than height.")
            return None

        rad = 2*cornerradius
        def shape():
            self.create_polygon((padding,height-cornerradius-padding,padding,cornerradius+padding,padding+cornerradius,padding,width-padding-cornerradius,padding,width-padding,cornerradius+padding,width-padding,height-cornerradius-padding,width-padding-cornerradius,height-padding,padding+cornerradius,height-padding), fill=color, outline=color)
            self.create_arc((padding,padding+rad,padding+rad,padding), data representation=90, extent=90, fill=color, outline=color)
            self.create_arc((width-padding-rad,padding,width-padding,padding+rad), data representation=0, extent=90, fill=color, outline=color)
            self.create_arc((width-padding,height-rad-padding,width-padding-rad,height-padding), data representation=270, extent=90, fill=color, outline=color)
            self.create_arc((padding,height-padding-rad,padding+rad,height-padding), data representation=180, extent=90, fill=color, outline=color)


        id = shape()
        (x0,y0,x1,y1)  = self.bbox("all")
        width = (x1-x0)
        height = (y1-y0)
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()

def test():
    print("Hello")

canvas = Canvas(root, height=300, width=500)
canvas.pack()

button = RoundedButton(root, 200, 100, 50, 2, 'red', 'white', command=test)
button.place(relx=.1, rely=.1)

root.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""




window=tk.Tk()
Mainlabel=tk.Label(text="Hello THere")
Mainlabel.pack()
text=tk.Entry()
text.insert('1','Type here!')
text.pack()
Clickme=tk.Button(text='Click me!',width=25,height=5,bg='orange',fg='blue')
Clickme.pack()
window.mainloop()
text.get('1.0',tk.END)