#https://edabit.com/challenge/8qD23E6XRMaWhyJ5z
def happiness_number(happiness):
    score=0

    if ":)" in happiness and "(:" in happiness:
        score+=2
    if ":(" in happiness and "):" in happiness:
        score-=2
    elif ":)" in happiness or "(:" in happiness:
        score+=1
    elif ":(" in happiness or "):" in happiness:
        score-=1
    elif happiness==None:
        pass
    else:
        pass
    print(score)



def happy(line):
    h1 = len(line.split(":)"))-1
    h2 = len(line.split("(:")) - 1
    s1 = len(line.split("):")) - 1
    s2 = len(line.split(":(")) - 1
    return h1+h2-s1-s2
happiness_number(":):(")
print(happy(":):("))