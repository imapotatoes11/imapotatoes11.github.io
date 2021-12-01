#https://edabit.com/challenge/cyzbSvpfSzDjGi4TB
def harmonic(a):
    total=0.0
    count=1
    for i in range(a):
        total+=float(1/count)
        count+=1
    return round(total,3)
print(harmonic(3))