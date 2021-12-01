import itertools
'''
NEED TO OPTIMIZE
USES TOO MUCH MEMORY
WRITE TO A TEMPORARY TXT FILE INSTEAD!!!
READ LINE 38!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
#a_list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26] CRASHES
a_list=[]
leng=int(input('max length:'))-1
try:
    for i in range(leng):
        a_list.append(i)
except:
    a_list=[1,2,3,4,5,6,7]
all_combinations=[]
for r in range(len(a_list)+1):
    #combinations_object=itertools.combinations(a_list,r)
    combinations_object=itertools.permutations(a_list,r)
    combinations_list=list(combinations_object)
    all_combinations+=combinations_list
    print("thinking...")
    print()
print(all_combinations)
with open('temp1.txt','w') as file:
    file.write(str(all_combinations))
del all_combinations
import convert
'''
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

CHANGE FINAL AND FINALE TO SEPARATE TXT FILES!!!

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
        file.write(f'\n{"".join(finale[i])}')'''