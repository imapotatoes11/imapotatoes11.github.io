#https://edabit.com/challenge/pKSL3HtApPYAJ72CJ
def name_shuffle(n):
    m=(n.split())
    m.reverse()
    return ' '.join(tuple(m))
print(name_shuffle('Donald Trump'))