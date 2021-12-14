'''
0 1 2
3 4 5
6 7 8
'''
import random,time
board=['-','-','-',
       '-','-','-',
       '-','-','-']
def pboard(b):
    print(b[0], b[1], b[2])
    print(b[3], b[4], b[5])
    print(b[6], b[7], b[8])


def check_board(board):
    # VERTICAL
    if board[2] == board[5] == board[8] == 'X': exec("pboard(board)\nprint('Player 1 wins!!!')\ninput('Press the enter key to close this window... ')\nexit(0)")
    if board[2] == board[5] == board[8] == 'O': exec("print('Player 2 wins!!!')\nexit(0)")

    if board[1] == board[4] == board[7] == 'X': exec("pboard(board)\nprint('Player 1 wins!!!')\ninput('Press the enter key to close this window... ')\nexit(0)")
    if board[1] == board[4] == board[7] == 'O': exec("print('Player 2 wins!!!')\nexit(0)")

    if board[0] == board[3] == board[6] == 'X': exec("pboard(board)\nprint('Player 1 wins!!!')\ninput('Press the enter key to close this window... ')\nexit(0)")
    if board[0] == board[3] == board[6] == 'O': exec("print('Player 2 wins!!!')\nexit(0)")
    # VERTICAL

    # HORIZONTAL
    if board[0] == board[1] == board[2] == 'X': exec("pboard(board)\nprint('Player 1 wins!!!')\ninput('Press the enter key to close this window... ')\nexit(0)")
    if board[0] == board[1] == board[2] == 'O': exec("print('Player 2 wins!!!')\nexit(0)")

    if board[3] == board[4] == board[5] == 'X': exec("pboard(board)\nprint('Player 1 wins!!!')\ninput('Press the enter key to close this window... ')\nexit(0)")
    if board[3] == board[4] == board[5] == 'O': exec("print('Player 2 wins!!!')\nexit(0)")

    if board[6] == board[7] == board[8] == 'X': exec("pboard(board)\nprint('Player 1 wins!!!')\ninput('Press the enter key to close this window... ')\nexit(0)")
    if board[6] == board[7] == board[8] == 'O': exec("print('Player 2 wins!!!')\nexit(0)")
    # HORIZONTAL

    # DIAGONAl
    if board[0] == board[4] == board[8] == 'X': exec("pboard(board)\nprint('Player 1 wins!!!')\ninput('Press the enter key to close this window... ')\nexit(0)")
    if board[0] == board[4] == board[8] == 'O': exec("print('Player 2 wins!!!')\nexit(0)")
    if board[8] == board[4] == board[0] == 'X': exec("pboard(board)\nprint('Player 1 wins!!!')\ninput('Press the enter key to close this window... ')\nexit(0)")
    if board[8] == board[4] == board[0] == 'O': exec("print('Player 2 wins!!!')\nexit(0)")

    if board[2] == board[4] == board[6] == 'X': exec("pboard(board)\nprint('Player 1 wins!!!')\ninput('Press the enter key to close this window... ')\nexit(0)")
    if board[2] == board[4] == board[6] == 'O': exec("print('Player 2 wins!!!')\nexit(0)")
    if board[6] == board[4] == board[2] == 'X': exec("pboard(board)\nprint('Player 1 wins!!!')\ninput('Press the enter key to close this window... ')\nexit(0)")
    if board[6] == board[4] == board[2] == 'O': exec("print('Player 2 wins!!!')\nexit(0)")

##########################################
#CORE LOOP
##########################################

win=False
p2=int(input("1 player or 2 player?: "))
while win==False:
    choice=int(input("Player 1 (X): "))
    board[choice]='X'
    check_board(board)
    if p2==1:
        board[random.randint(0,8)]='O'
        check_board(board)
    else:
        pboard(board)
        board[int(input("Player 2 (Y): "))]='O'
        pboard(board)
        check_board(board)


    check_board(board)
again=input('Play again? r to play again: ')
time.sleep(1)
if again=='r':
    import tictactoe.py
else:
    time.sleep(100000000)
    exit(0)
    input()
input()