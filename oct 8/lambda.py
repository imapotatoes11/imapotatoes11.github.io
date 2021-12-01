import random
# def biggest_number():
l2 = [random.randint(1,100) for e in range(20)]
l3 = range(1,5)
print(l2)
def process_list2(lst,how,r0):
    r = r0
    for e in lst:
        r = how(e,r)
    return r
print(process_list2(l2,lambda x,r:x if r is None or x>r else r,None))
print(process_list2(l2,lambda x,r:x if r is None or x<r else r,None))
print(process_list2(l2,lambda x,r:x+r,0))
print(process_list2(l3,lambda x,r:x*r,1))
print(process_list2(l3,lambda x,r:x*r^2,1))