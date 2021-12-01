length=int(input())
code=""
output=[]
for i in range(length):
    code=code+input()
    code.split()
    codee=list(code)
    codee.remove(" ")
    output.append(list(int(codee[i])*codee[i+1][i]))
print(output)