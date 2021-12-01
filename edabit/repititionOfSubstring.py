#https://edabit.com/challenge/wNMyGvSuBucrvHrmC
def number_of_repeats(line):
    l=len(line)
    for i in range(l,l+1):
        if i**2>l:
            break
        else:
            s=line[:i]
            n=l//i
            if (i*n)==l and s*n==line:
                return n
    return l
print(number_of_repeats("ababababab"))
print(number_of_repeats("abcabc"))