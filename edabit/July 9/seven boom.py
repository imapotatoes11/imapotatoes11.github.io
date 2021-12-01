#https://edabit.com/challenge/BokhFunYBvsvHEjfx
def seven_boom(a):
    contains=0
    for i in range(len(a)):
        for j in range(len(str(a[i]))):
            if '7' in str(a[i])[j]:
                contains+=1
                break
    return "Boom!" if contains<0 else "there is no 7 in the list"

print(seven_boom([1,2,3,4,5,6,8,9,78]))