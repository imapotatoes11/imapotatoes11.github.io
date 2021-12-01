#https://edabit.com/challenge/hFNhDGNt8CNjSNnG9
def setify(n):
    lst = list(dict.fromkeys(n))
    return lst
print(setify(['a','a']))