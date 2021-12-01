#https://edabit.com/challenge/MvgCxPkSgtQ8hQjwx
def remove_vowels(n):
    mydict = {#A
            97: 0,
              65: 0,
              #E
              101: 0,
              69: 0,
            #I
        105: 0,
        73: 0,
        #O
        111:0,
        79:0,
        #U
        117:0,
        85:0}
    txt = n
    print(txt.translate(mydict))
remove_vowels("I have never seen a thin person drinking Diet Coke.")
#print(remove_vowels("I have never seen a thin person drinking Diet Coke."))