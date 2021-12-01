#https://edabit.com/challenge/gt9LLufDCMHKMioh2
def stutter(word):
    return word[:2]+"... "+word[:2]+'... '+word+'?'
print(stutter("hello"))