yes=['1','4','8','56','75','19','3','4']
yess=len([i for i in yes if i=='4'])
print(yess)


yes=['1','4','8','56','75','19','3','4']

yess=[]
for i in yes:
    if i=='4':
        yess.append(i)
print(yess)