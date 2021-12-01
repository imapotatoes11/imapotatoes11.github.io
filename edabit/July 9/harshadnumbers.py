#https://edabit.com/challenge/ZDDyfBFBWMotQSYin
def is_harshad(a):
    total=0
    for i in range(len(str(a))):
        total+=int(str(a)[i])
    return True if a%total==0 else False
print(is_harshad(209))
print(is_harshad(41))
print(is_harshad(12255))