#https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements
import itertools

stuff = [0,1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
l=[]
ml=int(input("max length: "))+1
for L in range(0, ml):#len(stuff)+1
#for L in range(0, 5):
    for subset in itertools.permutations(stuff, L):
        #print(subset)
        #print(''.join([chr(lo+97) for lo in subset]))
        ll=[]
        for i in subset:
            #ll.append(chr(i+97))
            #UPPERCASE /\
            #LOWECASE \/
            ll.append(chr(i+65))
            #print(i+96)

            # autosave no worke
            '''with open('pwsolverv2.0.txt', 'a') as file:
                # file.write(str('\n'.join(l)))
                for i in range(len(l)):
                    file.write(f'\n{"".join(l[i])}')'''
        print(''.join(ll))
        l.append(ll)


#for i in range(97):
#    print(chr(i))
'''COMBINATIONS'''
for L in range(0, ml):#len(stuff)+1
#for L in range(0, 5):
    for subset in itertools.combinations(stuff, L):
        #print(subset)
        #print(''.join([chr(lo+97) for lo in subset]))
        ll=[]
        for i in subset:
            #ll.append(chr(i+97))
            #UPPERCASE /\
            #LOWECASE \/
            ll.append(chr(i+65))
            #print(i+96)

            # autosave no worke
            '''with open('pwsolverv2.0.txt', 'a') as file:
                # file.write(str('\n'.join(l)))
                for i in range(len(l)):
                    file.write(f'\n{"".join(l[i])}')'''
        print(''.join(ll))
        l.append(ll)
print(l)
sl = set()
for item in l:
    sl.add(''.join(item))
sl = set([''.join(i) for i in l])

with open('pwsolverv2.txt','w') as file:
    #file.write(str('\n'.join(l)))
    for i in l:#for i in sl:
        file.write(f'\n{"".join(i)}')
'''
with open('pwsolverv2.txt','a') as file:
    l=[]
    for subset in itertools.combinations(stuff, L):
        ll = []
        for i in subset:
            ll.append(chr(i + 65))
        print(''.join(ll))
        #l.append(ll)
        file.write('\n')
        file.write(''.join(ll))
        '''
#print(l)
print("done")
