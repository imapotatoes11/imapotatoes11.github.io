#https://edabit.com/challenge/gJSkZgCahFmCmQj3C
def de_nest(n):
    return str(n).strip(']').strip('[')
print(de_nest([[[[[['Hello']]]]]]))