list=[1,2,3,4,5,-1,-2,-3,-4,-5]
negatives=[]
for i in range(len(list)):
    if list[i]<0:
        negatives.append(list[i])
negatives.sort()
print(negatives)
print(sum(negatives))