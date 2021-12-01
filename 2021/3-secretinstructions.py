directions=[]
while True:
    inputt=int(input(""))
    firstsum=int(str(inputt)[0])-int(str(inputt)[1])
    if firstsum==0:
        direction=direction
    elif firstsum%2!=0:
        direction=("left",str(inputt[2:])[:])
    elif firstsum%2==0 and firstsum!=0:
        direction=("right",str(inputt[2:])[:])
    #direction=direction+(" "+str(direction[4:6]))
    directions.append(direction)
    if inputt==99999 or inputt=="99999":
        break
print(direction)