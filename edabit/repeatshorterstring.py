#https://edabit.com/challenge/dRjHygERcDJpiDzze
#currently not working
def lengthen(str1,str2):
    if str1>str2:
        longer=str1
        long=str2
    elif str2>str1:
        longer=str2
        long=str1
    longerS=[]
    longS=[]
    for i in range(len(longer)):
        longerS.append(longer[i])
    for j in range(len(long)):
        longS.append(long[j])
    out=""
    for l in range(10000):
        for k in range(len(long)):
            out+=long[k]
            if len(out)==len(longer):
                return out
def pritn(pritn):
    print(pritn)


def lengthenne(s1,s2):
    l1=len(s1)
    l2=len(s2)
    if l1>l2:
        n=l1//l2
        r=l1%l2
        return s2*n+s2[:r]
    else:
        lengthenne(s2,s1)
pritn(lengthen("hello","he"))
pritn(lengthenne("hello","he"))