import pygame
import random
from copy import deepcopy

pygame.init()
O = 1
X = 2
f1 = pygame.font.Font(None, 35)
f2 = pygame.font.SysFont('serif', 40)
f3 = pygame.font.SysFont('timesnewroman', 37)
f4 = pygame.font.SysFont('calibri', 25)
bloc = 3
size_blo = 160
midth = 15
ste = bool(random.randrange(0, 2))
wid = size_blo * bloc + midth * (bloc + 1)
heig = wid + size_blo + 20
titl_re = pygame.Rect(0, 0, wid, size_blo + 20)
dela_ke = 10
score_win = {'Blue': 0, 'Red': 0}
scor = True
win_line = [(0, 0), (0, 0)]
wi = False
lin = [[(0, 0)] * 3 for _ in range(3)]
mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pos = 5
Rungame = True


def RenderWindow():
    pygame.draw.rect(scr, (255, 235, 190), titl_re)
    ste = f3.render("Next step:", True, (10, 10, 10))
    te_red = f1.render(f"Red: {score_win['Red']}", True, (250, 0, 0))
    te_blue = f1.render(f"Blue: {score_win['Blue']}", True, (0, 0, 250))
    te = f2.render("Score:", True, (0, 0, 0))
    restart = f4.render("Click 'R' to restart", True, (40, 200, 35))
    scr.blit(ste, (240, 110))
    scr.blit(te, (25, 15))
    scr.blit(te_red, (40, 80))
    scr.blit(te_blue, (40, 125))
    if wi:
        scr.blit(restart, (330, 15))
    if ste:
        pygame.draw.rect(scr, (0, 0, 0), (415, 70, 90, 90))
        pygame.draw.rect(scr, (160, 160, 255), (420, 75, 80, 80))
        pygame.draw.circle(scr, (0, 0, 255), (420 + 40, 75 + 40), 35, 10)
    else:
        pygame.draw.rect(scr, (0, 0, 0), (415, 70, 90, 90))
        pygame.draw.rect(scr, (255, 160, 160), (420, 75, 80, 80))
        pygame.draw.line(scr, (255, 0, 0), (435, 85), (485, 145), 8)
        pygame.draw.line(scr, (255, 0, 0), (485, 85), (435, 145), 8)
    for row in range(bloc):
        for column in range(bloc):
            cursor = False
            x_draw = False
            o_draw = False
            color = (255, 255, 255)
            if row == y and column == x and not wi:
                cursor = True
                color = (130, 130, 130)
            if mat[row][column] == X:
                color = (255, 160, 160)
                if cursor and not wi:
                    color = (200, 100, 100)
                x_draw = True
            elif mat[row][column] == O:
                color = (160, 160, 255)
                if cursor and not wi:
                    color = (100, 100, 200)
                o_draw = True
            w = column * size_blo + (column + 1) * midth
            h = (row + 1) * size_blo + (row + 1) * midth + 20
            pygame.draw.rect(scr, color, (w, h, 160, 160))
            lin[row][column] = (w + 80, h + 80)
            if x_draw:
                pygame.draw.line(scr, (255, 0, 0), (w + 15, h + 10), (w + 145, h + 150), 22)
                pygame.draw.line(scr, (255, 0, 0), (w + 145, h + 10), (w + 15, h + 150), 22)
            elif o_draw:
                pygame.draw.circle(scr, (0, 0, 255), (w + 80, h + 80), 70, 24)
            if wi and not scor:
                pygame.draw.line(scr, (255, 0, 255), win_line[0], win_line[1], 10)
    pygame.display.flip()


def restart_game():
    global mat, wi, pos, ste, scor
    mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    wi = False
    pos = 5
    scor = True
    ste = bool(random.randrange(0, 2))
    scr.fill('black')


def find_win(win_cell, start, end):
    global win_line
    r = win_cell == X
    b = win_cell == O
    win_line = (lin[start[0]][start[1]], lin[end[0]][end[1]])
    return r, b


def run_tic_tac_toe():
    global dela_ke, ste, Rungame, scr, mat, pos, x, y
    scr = pygame.display.set_mode((wid, heig))
    pygame.display.set_caption("КРЕСТики  И  НОЛЬики: X-X-O")
    clock = pygame.time.Clock()
    while Rungame:
        clock.tick(30)
        if dela_ke > 0:
            dela_ke -= 1
        check_win()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Rungame = False
        keys = pygame.key.get_pressed()
        if wi and (keys[pygame.K_r] or keys[pygame.K_BACKSPACE]):
            restart_game()
        if keys[pygame.K_UP] and (pos - 3) >= 1 and dela_ke == 0 and not wi:
            dela_ke += 10
            pos -= 3
        elif keys[pygame.K_DOWN] and (pos + 3) <= 9 and dela_ke == 0 and not wi:
            dela_ke += 10
            pos += 3
        elif keys[pygame.K_RIGHT] and dela_ke == 0 and (pos - 1) // bloc == pos // bloc and not wi:
            dela_ke += 10
            pos += 1
        elif keys[pygame.K_LEFT] and dela_ke == 0 and (pos - 2) // bloc == (pos - 1) // bloc and not wi:
            dela_ke += 10
            pos -= 1
        y = (pos - 1) // bloc
        x = (pos - 1) % bloc
        if (keys[pygame.K_x] or keys[pygame.K_RETURN]) and not ste and mat[y][x] == 0 and not wi:
            mat[y][x] = X
            ste = True
        elif (keys[pygame.K_o] or keys[pygame.K_RETURN]) and ste and mat[y][x] == 0 and not wi:
            mat[y][x] = O
            ste = False
        RenderWindow()


def check_win():
    global score_win, wi, scor, x, y
    blue_win = red_win = False
    m = deepcopy(mat)

    no_zero = all(all(row) for row in m)
    for i in range(3):
        if m[i][0] == m[i][1] == m[i][2] and m[i][1]:
            red_win, blue_win = find_win(m[i][1], (i, 0), (i, 2))
    for j in range(3):
        if m[0][j] == m[1][j] == m[2][j] and m[1][j]:
            red_win, blue_win = find_win(m[1][j], (0, j), (2, j))
    if m[0][0] == m[1][1] == m[2][2]:
        red_win, blue_win = find_win(m[1][1], (0, 0), (2, 2))
    elif m[0][2] == m[1][1] == m[2][0]:
        red_win, blue_win = find_win(m[1][1], (0, 2), (2, 0))

    if red_win or blue_win or no_zero:
        wi = True
        x = y = 3
        if red_win and scor:
            score_win['Red'] += 1
            scor = False
        elif blue_win and scor:
            score_win['Blue'] += 1
            scor = False


if __name__ == '__main__':
    run_tic_tac_toe()
    pygame.quit()
