import random
wl=int(input("'1' win or '2' lose: "))
while True:
    rps=input("'r' rock, 'p' paper, or 's' scissors: ")
    if wl==1:
        if rps=='r':
            print('paper.')
            print('you lose!')
            print()
        if rps=='p':
            print('scissors.')
            print('you lose!')
            print()
        if rps=='s':
            print('rock.')
            print('you lose!')
            print()
    if wl==2:
        out=random.choice(['r','p','s'])
        if out=='r' and rps=='r' or out=='p' and rps=='p' or out=='s' and rps=='s':
            match out:
                case 'r':
                    print('rock.')
                case 'p':
                    print('paper.')
                case 's':
                    print('scissors')
            print('tie')
            print()
        if out=='r' and rps=='p':
            print('rock.')
            print('you win!')
            print()
        if out=='r' and rps=='s':
            print('rock.')
            print('you lose!')
            print()
        if out=='p' and rps=='r':
            print('paper.')
            print('you lose!')
            print()
        if out=='s' and rps=='r':
            print('scissors.')
            print('you win!')
            print()
        if out=='s' and rps=='p':
            print('scissors.')
            print('you lose!')
            print()
        if out=='p' and rps=='s':
            print('paper.')
            print('you win!')
            print()