#https://edabit.com/challenge/pimnBHXJNtQffq4Cf
def mapping(n):
    dic={}
    for i in range(len(n)):
        dic[n[i]]=(n[i].upper())
    return dic
print(mapping(['p','s']))