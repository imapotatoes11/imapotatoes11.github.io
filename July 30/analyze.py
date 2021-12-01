def analyze(*params):
    lst=list(params)
    return min(lst),max(lst),round(sum(lst)/len(lst),2),len(lst)
    #try to return min, max, average, count
    pass
print(analyze(1,2,3,4))
def checkTriangle(a,b,c):
    #return all below value:
    #whether if it is a triangle
    #what kind of triangle it is
    #if failed, reason
    #original parameter of a,b,c
    if a+b>c and b+c>a and a+c>b:
        return (True,None,[],(a,b,c))
    else:
        return (False,'INVALID_LENGTH_COMBINATION',None,(a,b,c))
    pass
