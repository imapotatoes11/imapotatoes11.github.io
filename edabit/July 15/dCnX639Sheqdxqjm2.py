#https://www.edabit.com/challenge/dCnX639Sheqdxqjm2
def parallel_resistance(a):
    import fractions as f
    count=0
    for i in a:
        count+=f.Fraction(1,int(a[i]))
    return count
print(parallel_resistance([6,3,6]))