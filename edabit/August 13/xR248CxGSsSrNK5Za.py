#https://edabit.com/challenge/xR248CxGSsSrNK5Za
def make_rug(m,n,s="#"):
    e=[]
    for i in range(m):
        e.append(s*n)
    return e
print(make_rug(3,5))