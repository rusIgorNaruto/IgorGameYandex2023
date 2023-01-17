import pygame
import pygame_widgets
import pygame_widgets.button as btn
from Snake.Game import run_snake
from TicTacToe.Game import run_tic_tac_toe

pygame.init()
okno = pygame.display.set_mode((800, 317))
clok = pygame.time.Clock()
fon = pygame.font.SysFont('Motel King', 90, bold=True)
tic = btn.Button(
    okno, 425, 75, 300, 150, text='Tic Tac',
    font=fon, fontSize=fon.get_ascent(),
    inactiveColour=(255, 36, 0), hoverColour=(0, 0, 255), margin=10, radius=10, onClick=run_tic_tac_toe)
snake = btn.Button(
    okno, 75, 75, 300, 150, text='Snake',
    font=fon, fontSize=fon.get_ascent(), inactiveColour=(130, 255, 0), hoverColour=(204, 78, 92), margin=10, radius=10,
    onClick=run_snake)
run = True
while run:
    okno = pygame.display.set_mode((800, 317))
    pygame.display.set_caption('Game')
    okno.fill((128, 128, 128))
    ev = pygame.event.get()
    for i in ev:
        if i.type == pygame.QUIT:
            run = False
    pygame_widgets.update(ev)
    [btn.listen(ev) for btn in [snake, tic]]
    [btn.draw() for btn in [snake, tic]]
    pygame.display.flip()
    clok.tick(120)
pygame.quit()
