def processLine(inputLine):
    lst=[]
    lC = None
    count = 0
    for i,c in enumerate(inputLine):
        if lC==None:
            lC=c
            count=1
        elif lC==c:
            count=count+1
        elif lC!=c:
            lst.append(f'{count} {lC}')
            lC=c
            count=1
    lst.append(f'{count} {lC}')
    print(' '.join(lst))

N = int(input())
for i in range(N):
    processLine(input())
