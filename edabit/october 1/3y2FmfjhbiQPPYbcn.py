#https://edabit.com/challenge/3y2FmfjhbiQPPYbcn
def pop(n):
    final=[]
    for i in range(len(n)):
        e=False
        if n[i]!=0:
            e=True
            num=n[i]
            final.append(n[i])
            #not done(here)
        if e==False:
            final.append(0)
