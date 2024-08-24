import pygame
from pygame.locals import *
pygame.init()

window= pygame.display.set_mode((600,600))

window.fill((0,0,0))
rect_positions=[]
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        elif event.type==MOUSEBUTTONUP:
            position=event.pos
            rect_positions.append(position)
    for position in rect_positions:
        rect=pygame.draw.rect(window, (255, 255, 255), [position[0], position[1], 10, 70], 0)
    pygame.display.update()