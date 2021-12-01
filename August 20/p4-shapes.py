import pygame
import math


pygame.init()
scr = pygame.display.set_mode((800,600))
mode=None
dots=[]



color = (0,0,255)
running = True

count = 0

def draw():
    global mode
    for i in range(7):
        if mode==0:
            dots.append([(i * 100 + 100, 200), (255, 0, 0), 10])
        if mode==1:
            dots.append([(i * 100 + 100, 300), (255, 0, 0), 10])
        if mode==2:
            dots.append([(i * 100 + 100, 0), (255, 0, 0), 10])
        else:
            dots.append([(i * 100 + 100, 400), (255, 0, 0), 10])
    scr.fill((255, 255, 255))
    for dot in dots:
        pygame.draw.circle(scr, dot[1], dot[0], dot[2])
def update():
    for i, dot in enumerate(dots):
        if i < 2:
            if count % 100 < 50 :
                dot[0] = (dot[0][0] - 1, dot[0][1] - 1)
            else:
                dot[0] = (dot[0][0] + 1, dot[0][1] + 1)
def main_loop():
    global running
    global count
    while running:
        count+=1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        update()

        draw()

        pygame.display.flip()






main_loop()
pygame.quit()
