#https://edabit.com/challenge/qM6zWQM7gdfPgE9Hh
def filter_by_rating(dic,star):
    for i in dic:
        inv_map = {v: k for k, v in dic.items()}
        #trying to make STR.TRANSLATE TO WORK
        eff=i.translate(inv_map)
        print((i.translate(dic)))
        if i==star:
            print("ESFOHEODIUFHOIRHD")
        else:
            print("no")
filter_by_rating({"ef":"*****","hp":"***"},"***")