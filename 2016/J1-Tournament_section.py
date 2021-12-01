#NOT WORKING
win=[]
for i in range(6):
    win.append(input())
Final=0
for j in range(len(win)):
    if win[j].lower=="w":
        Final+=1
if Final==5 or Final==6:
    print(3)
elif Final==3 or Final==4:
    print(2)
elif Final==2 or Final==1:
    print(1)
elif Final<=6:
    print(3)
else:
    print(-1)