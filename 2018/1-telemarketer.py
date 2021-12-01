answer=[]
digit1=int(input())
digit2=int(input())
digit3=int(input())
digit4=int(input())
if digit1==8 or digit1==9:
    answer.append(True)
else:
    answer.append(False)

if digit2==digit3:
    answer.append(True)
else:
    answer.append(False)

if digit4==8 or digit4==9:
    answer.append(True)
else:
    answer.append(False)


if answer==[True,True,True]:
    print("ignore")
else:
    print("answer")