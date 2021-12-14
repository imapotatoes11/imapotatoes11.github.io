'''def guess():
    import random
    num, score = random.randint(1, int(input("random number chance: 1/"))), 100
    while int(input("guess number: ")) != num: score -= 1
    if (input(f'yes it was indeed {str(num)}\nYour score was {str(score)} (100 is the best)\nr to play again: ')).lower() == 'r': guess()

def guesslong():
    import random
    num=random.randint(1,int(input("random number chance: 1/")))
    score=100
    while True:
        guess=int(input("guess number: "))
        if guess==num:
            print(f'yes it was indeed {str(num)}')
            break
    print(f'Your score was {str(score)} (100 is the best)')
    again=input('r to play again:')
    if again=='r':
        guesslong()
'''

import random
num,score=random.randint(1,int(input("random number chance: 1/"))),100
while int(input("guess number:"))!=num: score-=1
if (input(f'yes it was indeed {str(num)}\nYour score was {str(score)} (100 is the best)\nr to play again: ')).lower()=='r': import guessnumber.py