#https://edabit.com/challenge/6DwrhEGSa6WDixA5u
def is_narcissistic(n):
    count=0
    for i in range(len(str(n))):
        count+=int(str(n)[i])**len(str(n))
    #return [int(x)**len(list(str(n))) for x in list(str(n))]
    return count==n
print(is_narcissistic(153))
print(is_narcissistic(22))