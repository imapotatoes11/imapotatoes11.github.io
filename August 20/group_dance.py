import pygame
import math


pygame.init()
scr = pygame.display.set_mode((800,600))

dots=[]
for i in range(7):
    dots.append([(i*100+100,200),(255,0,0),30])


color = (0,0,255)
running = True

count = 0
mode = 0

def draw():
    scr.fill((255, 255, 255))
    for dot in dots:
        pygame.draw.circle(scr, dot[1], dot[0], dot[2])


def update():
    global mode
    if mode==1:
        for i, dot in enumerate(dots):
            if count % 100 < 50:
                dot[0] = (dot[0][0] - 1, dot[0][1] - 1)
            else:
                dot[0] = (dot[0][0] + 1, dot[0][1] + 1)
    elif mode==2:
        for i, dot in enumerate(dots):
            if count % 100 < 50:
                dot[2] += 1
            else:
                dot[2] -= 1

def event_handler():
    global running
    global mode
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                mode = 0
            elif event.key == pygame.K_1:
                mode = 1
            elif event.key == pygame.K_2:
                mode = 2
        elif event.type == pygame.QUIT:
            pygame.quit()
            quit()

def main_loop():
    global running
    global count
    while running:
        count+=1

        event_handler()
        update()

        draw()

        pygame.display.flip()






main_loop()
pygame.quit()