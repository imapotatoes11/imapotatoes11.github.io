#https://edabit.com/challenge/sEChDwmcHvWcMSmRM
def find_the_falsehoods(a):
    return [x for x in a if not x]
print(find_the_falsehoods([[],2,4,2]))