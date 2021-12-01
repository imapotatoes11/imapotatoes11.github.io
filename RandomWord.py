import random as r
#clear file to prepare for reading in lines 221-235
import time

with open('RandomWord.txt','w') as file:
    file.write('')
def generate(length):
    vowel=['a','e','i','o','u']
    consonant=['b','c','d','f','g','h','j','k','k','l','m','n','p','q','r','s','t','v','w','x','z']
    ending=['e','y','a']
    combination=['ch','th','nd']

    tf=[True,False]
    rr=r.choice(tf)
    rr2=r.choice(tf)
    cchan=r.choice(tf)
    #if length==1
    if length==1:
        if rr:
            l1=r.choice(vowel)
        else:
            l1=r.choice(consonant)
        return l1
    #start
    if rr:
        l1=r.choice(vowel)
    else:
        l1=r.choice(consonant)

    #if u
    while l1=="u":
        if rr:
            l1=r.choice(vowel)
        else:
            l1=r.choice(consonant)

    #middle
    if rr:
        l2=r.choice(consonant)
        if length==2:
            return ''.join([l1,l2])
        if rr2:
            l3=l2
            if length==3:
                return ''.join([l1,l2,l3])
        else:
            l3=r.choice(vowel)
            if length==3:
                return ''.join([l1,l2,l3])
    if rr!=True:
        l2=r.choice(vowel)
        if length==2:
            return ''.join([l1,l2])
        if rr2:
            l3=l2
            if length==3:
                return ''.join([l1,l2,l3])
        else:
            l3=r.choice(consonant)
            if length==3:
                return ''.join([l1,l2,l3])

    #if more than 4 characters
    if length==4:
        pass
    elif length==5:
        # middle
        if rr:
            l5 = r.choice(vowel)
            if rr2:
                l6 = l5
            else:
                l6 = r.choice(consonant)
        if rr != True:
            l5 = r.choice(consonant)
            if rr2:
                l6 = l5
            else:
                l5 = r.choice(vowel)
    elif length==6:
        #1
        # middle
        if rr:
            l5 = r.choice(vowel)
            if rr2:
                l6 = l5
            else:
                l6 = r.choice(consonant)
        if rr != True:
            l5 = r.choice(consonant)
            if rr2:
                l6 = l5
            else:
                l5 = r.choice(vowel)


        #2
        # middle
        if rr:
            l7 = r.choice(vowel)
            if rr2:
                l6 = l7
            else:
                l7 = r.choice(consonant)
        if rr != True:
            l6 = r.choice(consonant)
            if rr2:
                l7 = l6
            else:
                l7 = r.choice(vowel)
    elif length==7:
        # 1
        # middle
        if rr:
            l5 = r.choice(vowel)
            if rr2:
                l6 = l5
            else:
                l6 = r.choice(consonant)
        if rr != True:
            l5 = r.choice(consonant)
            if rr2:
                l6 = l5
            else:
                l5 = r.choice(vowel)

        # 2
        # middle
        if rr:
            l7 = r.choice(vowel)
            if rr2:
                l6 = l7
            else:
                l7 = r.choice(consonant)
        if rr != True:
            l6 = r.choice(consonant)
            if rr2:
                l7 = l6
            else:
                l7 = r.choice(vowel)


        #3
        # 2
        # middle
        if rr:
            l8 = r.choice(vowel)
            if rr2:
                l9 = l8
            else:
                l8 = r.choice(consonant)
        if rr != True:
            l8 = r.choice(consonant)
            if rr2:
                l9 = l8
            else:
                l8 = r.choice(vowel)
    elif length==8:
        # 1
        # middle
        if rr:
            l5 = r.choice(vowel)
            if rr2:
                l6 = l5
            else:
                l6 = r.choice(consonant)
        if rr != True:
            l5 = r.choice(consonant)
            if rr2:
                l6 = l5
            else:
                l5 = r.choice(vowel)

        # 2
        # middle
        if rr:
            l7 = r.choice(vowel)
            if rr2:
                l6 = l7
            else:
                if cchan:
                    l7 = r.choice(combination)
        if rr != True:
            l6 = r.choice(consonant)
            if rr2:
                l7 = l6
            else:
                l7 = r.choice(vowel)

        # 3
        # 2
        # middle
        if rr:
            l8 = r.choice(vowel)
            if rr2:
                l9 = l8
            else:
                if cchan:
                    l8 = r.choice(combination)
        if rr != True:
            l8 = r.choice(consonant)
            if rr2:
                l9 = l8
            else:
                l8 = r.choice(vowel)



    #end
    l4=r.choice(ending)

    #compile
    l=[l1,l2,l3,l4]
    if length==4:
        pass
    if length==5:
        l.append(l5)
    if length==6:
        l.append(l5)
        l.append(l6)
    if length==7:
        l.append(l5)
        l.append(l6)
        l.append(l7)
    if length==8:
        l.append(l5)
        l.append(l6)
        l.append(l7)
        l.append(l8)
    #compilation substituded for the above brand new match-case keyword things
    '''
    if length==4:
        l=[l1,l2,l3,l4]
    if length==5:
        l=[l1,l2,l3,l4,l5]
    if length==6:
        l=[l1,l2,l3,l4,l5,l6]
    if length==7:
        l=[l1,l2,l3,l4,l5,l6,l7]
    '''
    return ''.join(l)

results=[]

try:
    many=int(input("How many to generate (only applies to multiple words, between 1000-10000, default 1000)? >>:"))
except:
    many=1000
onel=int(input("One and two letter words?\n'1' for yes, '2' for no:"))
if onel==1:
    leng=[1,2,3,4,5,6,7]
if onel==2:
    leng=[3,4,5,6,7]
else:
    leng=[1,2,3,4,5,6,7]
for i in range(many):#should be 1000
    results.append(generate(r.choice(leng)))
#check if word is in english dictionary
#https://stackoverflow.com/questions/3788870/how-to-check-if-a-word-is-an-english-word-with-python
#PRE_GUI\/
import PySimpleGUI as sg
layout=[[sg.Text("How many words to generate?")],
        [sg.Button("One Word"),sg.Button("Multiple Words")]]
window=sg.Window("RandomWord Inquiry",layout,resizable=True)
no=False
on=False
one=False
while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        no=True
        break
    if event=="One Word":
        on=True
        one=True
        break
    if event=="Multiple Words":
        on=True
        one=False
        break
window.close()

if no:
    exit(KeyboardInterrupt("Program Exited."))


#PRE_GUI/\
import enchant
from PyDictionary import PyDictionary
pd=PyDictionary()
d=enchant.Dict("en_US")
word_result=[]
for ii in range(len(results)):
    if d.check(results[ii]):
        #print(results[ii])
        word_result.append(results[ii])
        #print(pd.meaning(results[ii]))
        #print()
        if on:
            if one:
                with open('RandomWord.txt','w') as file:
                    file.write(f'\n{results[ii]}: {pd.meaning(results[ii])}')
            if one==False:
                with open('RandomWord.txt','a') as file:
                    file.write(f'\n{results[ii]}: {pd.meaning(results[ii])}')
with open('RandomWord.txt','r') as file:
    print(file.read())
print("consult randomword.txt")

import webbrowser
webbrowser.open("RandomWord.txt")
time.sleep(4)

import py_compile as pc
pc.compile('RandomWord.py',cfile='RandomWord.pyc')