#https://edabit.com/challenge/BZ4mMcEz3aqosEtbC
def mean(a):
    a=str(a)
    e=[]
    for i in range(len(a)):
        e.append(int(a[i]))
    se=sum(e)
    return se/len(a)