#https://edabit.com/challenge/kgMEhkNNjRmBTAAPz
def remove_special_characters(word):
    lst=[char for char in word]
    specials=['.','!','@','#','$','%','^','&','\\','*','(',')']
    for special in specials:
        try:
            lst.remove(special)
        except:
            pass
    return ''.join(lst)
print(remove_special_characters('Hello!'))