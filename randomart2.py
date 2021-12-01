from turtle import *
import random as r
import time as t
from datetime import datetime, date
start=t.time()
for i in range(10):
    speed(0)
    color1=r.choices(["red","orange","yellow","green","blue","magenta", "deep pink", "blue violet", "medium spring green", "lemon chiffon", "cyan", "midnight blue", "maroon", "lavender", "crimson", "pale green"])
    color2=r.choices(["red","orange","yellow","green","blue","magenta", "deep pink", "blue violet", "medium spring green", "lemon chiffon", "cyan", "midnight blue", "maroon", "lavender", "crimson", "pale green"])
    if color1==color2:
        color2=r.choices(["red","orange","yellow","green","blue","magenta", "deep pink", "blue violet", "medium spring green", "lemon chiffon", "cyan", "midnight blue", "maroon", "lavender", "crimson", "pale green"])
    color(color1, color2)
    begin_fill()
    length=r.randint(100,200)
    angle1=r.randint(90,350)
    angle2=r.randint(1,2)
    forbac=r.randint(1,2)
    while True:
        if forbac==1:
            forward(length)
        if forbac==2:
            backward(length)
        if angle2==1:
            left(angle1)
        if angle2==2:
            right(angle1)
        if abs(pos()) < 1:
            break
    end_fill()
    t.sleep(0)
    clear()
    goto(0,0)
end=t.time()


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today=date.today()

print(str(round((end-start),2))+" seconds")
scores=open("scores.txt","a")
scores.write("\n"+str(round((end-start),2))+" sec @ "+str(current_time)+" on "+str(today))
scores.close()
"""
from turtle import*
import random as r
color1=r.choices(["red","orange","yellow","green","blue","magenta"])
color2=r.choices(["red","orange","yellow","green","blue","magenta"])
color(color1, color2)
begin_fill()
penup()
goto(100, 200)
pendown()
goto(-100, 200)
goto(-100, -200)
goto(100, -200)
goto(100,200)
end_fill()
done()"""