def permutations(lst):
    import itertools
    return list(itertools.permutations(lst))
def enumerate_subsets(n):
    from itertools import chain, combinations
    s=list(n)
    return list(chain.from_iterable(combinations(s,r) for r in range(len(s)+1)))
def gcd(a,b):
    #import math
    #return math.gcd(n)
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)
def pascaltriangle(row,index):
    if row+1==1 or index+1==1 or row==index:
        return 1
    else:
        return pascaltriangle(row-1,index-1)+pascaltriangle(row-1,index)
print(permutations([1,2,3]))
print(enumerate_subsets([1,2,3]))
print(gcd(46,87))
print(pascaltriangle(5,3))