#https://edabit.com/challenge/Rbs2G5PaJtmYdLTJM
def is_heteromecic(d):
    count=0
    for i in range(10000):
        count+=1
        if count+(count+1)==d:
            return False
    return True
print(is_heteromecic(0))
print(is_heteromecic(2))
print(is_heteromecic(7))
print(is_heteromecic(110))