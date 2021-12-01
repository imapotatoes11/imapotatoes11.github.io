#https://edabit.com/challenge/JiLom4d6aBk7wAJcZ
def is_sastry(n):
    result=int(str(n)+str(n+1))**0.5
    return result==int(result)
print(is_sastry(183))
print(is_sastry(184))
print(is_sastry(106755))