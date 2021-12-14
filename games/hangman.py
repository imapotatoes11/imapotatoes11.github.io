import random
find_word=[]
with open('all_english_words.txt','r') as file:
    for i in file.readlines():
        find_word.append(i.removesuffix('\n'))
ww=random.choice(find_word)

word=[i for i in ww]
wordEncrypt=['*' for i in ww]
print(' '.join(wordEncrypt))
t=False
wrong=0
while t==False:
    letter=input("guess a letter: ")
    if letter in word:
        print('yes')
    else:
        print('no')
        wrong+=1
        print(f'{wrong}/10 wrong guesses')
        if wrong>=11:
            print('over!')
            t=True
            break
    for i in range(len(word)):
        if word[i]==letter:
            wordEncrypt[i]=letter
    print(' '.join(wordEncrypt))
    if '*' not in wordEncrypt:
        break
if t:
    print(f'noooooooooooo\nthe word was {word}')
else:
    print(f'yeye it was indeed {word}')
    print(f'{wrong} wrong guesses')