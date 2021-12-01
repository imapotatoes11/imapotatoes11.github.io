N=int(input())
coords=[]
for i in range(N):
    coords.append(str(input()))
    coords[i].split(",")
    for j in range(len(coords)):
        coords[j]=list(coords[j])
        coords[j]=list(coords[j])
    if coords[i][0]<10:
        jj=True
    if coords[i][0]>=10:
        jj=False
    print(jj)
xValues=[]
for l in range(len(coords)):
    xValues.append(coords[l][0])
    maxX=max(xValues)


yValues=[]
for ii in range(len(coords)):
    yValues.append(coords[ii][1])
    maxY=max(yValues)
maxCoords=list((xValues,yValues))


minX=min(xValues)
minY=min(yValues)

print("MIN X,Y: "+str(tuple((minX,minY))))
print("MAX X,Y: "+str(tuple((maxX,maxY))))
