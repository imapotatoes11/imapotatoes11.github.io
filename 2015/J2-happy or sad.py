line=input()
happy=0
sad=0
for i in range(len(line)):
    try:
        line.replace(":-)","",1)
        happy+=1
    except:
        pass

    try:
        line.replace("(-:","",1)
        happy+=1
    except:
        pass

    try:
        line.replace(")-:","",1)
        sad+=1
    except:
        pass

    try:
        line.replace(":-(","",1)
        sad+=1
    except:
        pass
if happy-sad>0:
    print("happy")
elif happy-sad<0:
    print("sad")
elif happy-sad==0:
    print("unsure")
else:
    print("none")