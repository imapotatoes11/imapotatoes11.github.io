#https://edabit.com/challenge/QiPr3M5tsqfsbYcCQ
def square_digits(n):
    numbers=[]
    for i in range(len(str(n))):
        numbers.append(int(str(n)[i])**2)
    return int((((str(numbers).replace(",","")).replace("[","")).replace("]","")).replace(" ",""))
print(square_digits(9119))