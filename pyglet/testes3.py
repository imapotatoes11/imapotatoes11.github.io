import time

import pyglet
from pyglet.window import key,mouse


#colors?
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'




window = pyglet.window.Window()
message=[]
@window.event
def on_key_press(symbol, modifiers):
    global message
    if symbol==key.F1:
        message.append(bcolors.ENDC)
    if symbol==key.F2:
        message.append(bcolors.OKBLUE)
    if symbol==key.F3:
        message.append(bcolors.OKCYAN)
    if symbol==key.F4:
        message.append(bcolors.OKGREEN)
    if symbol==key.F5:
        message.append(bcolors.WARNING)
    if symbol==key.F6:
        message.append(bcolors.FAIL)
    if symbol==key.F11:
        message.append(bcolors.BOLD)
    if symbol==key.F12:
        message.append(bcolors.UNDERLINE)
    if symbol == key.A:
        message.append('A')
    if symbol == key.B:
        message.append('B')
    if symbol == key.C:
        print('C')
        message.append('C')
    if symbol==key.D:
        message.append('D')
    if symbol==key.E:
        message.append('E')
    if symbol==key.F:
        message.append('F')
    if symbol==key.G:
        message.append('G')
    if symbol==key.H:
        message.append('H')
    if symbol==key.I:
        message.append('I')
    if symbol==key.J:
        message.append('J')
    if symbol==key.K:
        message.append('K')
    if symbol==key.L:
        message.append('L')
    if symbol==key.M:
        message.append('M')
    if symbol==key.N:
        message.append('N')
    if symbol==key.O:
        message.append('O')
    if symbol==key.P:
        message.append('P')
    if symbol==key.Q:
        message.append('Q')
    if symbol==key.R:
        message.append('R')
    if symbol==key.S:
        message.append('S')
    if symbol==key.T:
        message.append('T')
    if symbol==key.U:
        message.append('U')
    if symbol==key.V:
        message.append('V')
    if symbol==key.W:
        message.append('W')
    if symbol==key.X:
        message.append('X')
    if symbol==key.Y:
        message.append('Y')
    if symbol==key.Z:
        message.append('Z')
    if symbol==key.SPACE:
        message.append(' ')
    if symbol==key.NUM_0:
        message.append('0')
    if symbol==key.NUM_1:
        message.append('1')
    if symbol==key.NUM_2:
        message.append('2')
    if symbol==key.NUM_3:
        message.append('3')
    if symbol==key.NUM_4:
        message.append('4')
    if symbol==key.NUM_5:
        message.append('5')
    if symbol==key.NUM_6:
        message.append('6')
    if symbol==key.NUM_7:
        message.append('7')
    if symbol==key.NUM_8:
        message.append('8')
    if symbol==key.NUM_9:
        message.append('9')
    if symbol==key.NUM_0:
        pass
        #automatically appends 0 to message for some reason even if the if statement HAS NOTHING IN IT
    if symbol==key.NUM_ADD:
        message.append('+')
    if symbol==key.NUM_SUBTRACT:
        message.append('-')
    if symbol==key.NUM_MULTIPLY:
        message.append('*')
    if symbol==key.NUM_DIVIDE:
        message.append('/')
    if symbol == key.ENTER:
        print('The enter key was pressed.')
        message.append('\n')
    if symbol==key.COMMA:
        message.append(',')
    if symbol==key.PERIOD:
        message.append('.')
    if symbol==key.QUOTELEFT:
        message.append('`')
    if symbol==key.APOSTROPHE:
        message.append("'")
    if symbol==key.BACKSPACE:
        try:
            del message[-1]
            print(f'deleting {message[-1]}')
        except:
            print('message delete character failure')
            raise SyntaxError(bcolors.FAIL+bcolors.BOLD+'\n\n\n\n\n\n\n**********!!WARNING!!**********'+bcolors.BOLD+bcolors.HEADER+'\n\n\n\nError deleting last character of "{message}".\nPlease rerun and make sure there is at least 2 characters in the text before backspacing.')
    if symbol==key._1:
        message.append('!')
    if symbol==key._2:
        message.append('@')
    if symbol==key._3:
        message.append('#')
    if symbol==key._4:
        message.append('$')
    if symbol==key._5:
        message.append('%')
    if symbol==key._6:
        message.append('^')
    if symbol==key._7:
        message.append('&')
    if symbol==key._8:
        message.append('*')
    if symbol==key._9:
        message.append('(')
    if symbol==key._0:
        message.append(')')


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')
        message.append('left mouse click')
    if button == mouse.RIGHT:
        print('The right mouse button was pressed')
        message.append('right mouse click')
    if button == mouse.MIDDLE:
        print('The middle mouse button was pressed')
        message.append('middle mouse click')

@window.event
def on_draw():
    window.clear()

pyglet.app.run()
print(''.join(message))