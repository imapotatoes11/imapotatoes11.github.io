#https://edabit.com/challenge/NgSdtW84XFAnSwAie
def largest_swap(a):
    one,two=str(a[1]),str(a[0])
    total=int(one+two)
    if a>total:
        return True
    elif a<total:
        return False