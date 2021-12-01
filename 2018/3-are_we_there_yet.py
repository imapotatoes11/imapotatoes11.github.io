line1=input()
line1=list(line1.split(" "))
line=[]
line=[int(x) for x in line1]
output=0
for i in range(len(line)):
    output=""
    for j in range(len(line)):
        #This line does not yet work
        output+=" "+str((line[i]-line[j]))
    print(output)


"""
3 10 12 5
"""
"""
0  3 13 25 30
3  0 19 22 27
13 10 0 12 17
25 22 12 0  5
30 27 17 5  0
"""