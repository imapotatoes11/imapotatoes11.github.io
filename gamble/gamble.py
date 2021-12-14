import random,time
while True:
    print('\n\n\n\n\n\n\n')
    p=input('press the enter key to start... ')
    print('"1" for 50/50 chances')
    print('"2" for smaller chances')
    print('"3" for high stakes')
    choice=int(input(">>: "))
    if choice==1:
        while True:
            print()
            print('type "e" to exit')
            od=input("odd or even?: ")
            res=random.randint(2,11)
            if od=='e':
                break
            print('thinking... ')
            time.sleep(1)
            print('thinking... ')
            time.sleep(0.5)
            if res%2==0 and od=='even':
                print()
                print(f'the number was {res}, so you got it correct!')
            if res%2!=0 and od=='odd':
                print()
                print(f'the number was {res}, so you got it correct!')
            else:
                print()
                print('sorry, not a winner. Try again!')
    if choice==2:
        while True:
            print()
            print('type "e" to exit')
            od=input("guess the number, 1-10: ")
            if od=='e':
                break
            od=int(od)
            res=random.randint(1,10)
            if od==res:
                print()
                print(f'the number {od} is correct')
            else:
                print()
                print('sorry, not a winner. Try again!')
    if choice==3:
        while True:
            print()
            print('type "e" to exit')
            od=input("guess the number, 1-30: ")
            if od=='e':
                break
            od=int(od)
            res=random.randint(1,30)
            if od==res:
                print()
                print(f'the number {od} is correct')
            else:
                print()
                print('sorry, not a winner. Try again!')