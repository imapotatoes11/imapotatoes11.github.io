import time,random

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
# Functions used to find the word in order of use


#############
#get words
#############
print('collecting words...')
from english_words import english_words_set as es
es=list(es)
with open('all_english_words.txt','r') as file:
    ye=file.readlines()
es=[]
for i in range(len(ye)):
    ye[i].replace(r'\n','')
es=[i.removesuffix('\n') for i in ye]
#############
#get words
#############
slow=[]
time=[]
while True:
    word=random.choice(es)
    print()
    print()
    print('type these words as fast as you can')
    r=input("e to exit: ")
    if r=='e':
        break
    ts=time.time()
    o=input(f"{word.lower()}\n")
    te=time.time()
    if o.lower()==word.lower():
        print(f'completed at {round(te-ts,2)} seconds!')
        if round(te-ts,2)<=3:
            print('wow such fast')
            slow.append(False)
            time.append(round(te-ts,2))

        if round(te-ts,2)>3:
            print('wow such slow\nsuch dissapointment')
            slow.append(False)
            time.append(round(te - ts, 2))
    else:
        print('not correct')
        slow.append(True)
t=0
f=0
for i in slow:
    if i:
        f+=1
    else:
        t+=1
print()
print(f'{t} correct words\n{f} messed up words')
if f==0:
    print(bcolors.OKBLUE+'100% accuracy!'+bcolors.ENDC)
    exit(0)
print(f'{round((f/(t+f)),2)*100}% accuracy')