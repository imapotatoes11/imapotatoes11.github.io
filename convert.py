with open('temp1.txt','r') as file:
    ye=file.readlines()
print(ye)
ye.append('ye')
print(ye)
yes=ye[0]
yas=ye[0]
print(yas)
yo=[]
yass='yo='+yas
exec(yass)
print(yo)
all_combinations=yo






def toStr(n,base):
   #convertString = "0123456789ABCDEF"
   convertString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]


final=[]
finale=[]
with open('temp1.txt','w') as file:
    file.write('')
with open('temp2.txt','w') as file:
    file.write('')
'''
CHANGE FINAL AND FINALE TO SEPARATE TXT FILES!!!
'''
for i in range(len(all_combinations)):
    #final.append(toStr(list(all_combinations[i]),26))
    all_combinations[i]=list(all_combinations[i])
for i in range(len(all_combinations)):
    #with open('temp1.txt','a') as finala:
    for j in range(len(all_combinations[i])):
        final.append(toStr(all_combinations[i][j],26))
        #finala.write(f'\n{toStr(all_combinations[i][j], 26)}')
    #with open('temp1.txt','r') as file:
    #    list_of_lists=[]
    #    list_of_lists.append(file.readlines())
    print("fhaoeshfouashergd\nragsagd\narsfgsa\narsfgd\narsgfd\nrasgfd\nasrdg\naersdg\nasergd\nasdg\nasredg\nasrdga\naesgd\naesdg\nasreged\nasedg")
    #print(list_of_lists)
    #finale.append(list_of_lists)
    finale.append(final)
    print(finale)
    #finale.append(final)
    final=[]
print(final)
print(finale)
with open('pwsolve.txt','w') as file:
    for i in range(len(finale)):
        file.write(f'\n{"".join(finale[i])}')