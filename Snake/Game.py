import pygame
from random import randrange


def run_snake():
    pygame.init()

    factor = 45
    size = (factor * 22)
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption('Snake')
    cloc = pygame.time.Clock()
    staybg = False
    bg = pygame.image.load('bg/snake-space-bg.jpg')
    fon_scor = pygame.font.Font('fonts/font_pixel.ttf', round(size / 29.7))
    fon_end = pygame.font.Font('fonts/font_pixel.ttf', round(size / 12.5))
    x, y = randrange(0, size, factor), randrange(0, size, factor)
    apple = randrange(0, size, factor), randrange(0, size, factor)
    snake = [(x, y)]
    snake_length = 1
    dx = dy = score = 0
    moved = True
    anim_count, anim_speed = 0, 100
    RUN = True
    while RUN:
        if staybg:
            screen.blit(bg, (0, 0))
        else:
            screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                staybg = not staybg
        screen.blit(fon_scor.render(f'SCORE: {score}', False, "orange"), (15, 5))
        for pos in snake[:-1]:
            pygame.draw.rect(screen, 'green', (pos[0] + 1, pos[1] + 1, factor - 2, factor - 2))
        pygame.draw.rect(screen, (20, 255, 120), (snake[-1][0] + 1, snake[-1][1] + 1, factor - 2, factor - 2))
        pygame.draw.rect(screen, 'red', (apple[0] + 1, apple[1] + 1, factor - 2, factor - 2))
        if snake[-1] == apple:
            while apple in snake: apple = randrange(0, size, factor), randrange(0, size, factor)
            snake_length += 1
            anim_speed -= 3
            score += 1
        anim_count += 10
        if anim_count >= anim_speed:
            anim_count = 0
            x += dx * factor
            y += dy * factor
            snake.append((x, y))
            snake = snake[-snake_length:]
            moved = True
        if len(snake) != len(set(snake)) or min(x, y) < 0 or max(x, y) > size - factor:
            end_text = fon_end.render('GAME OVER!', False, "orange")
            screen.blit(end_text, ((size - end_text.get_width()) // 2, (size - end_text.get_height()) // 2))
            pygame.display.flip()
            while pygame.event.wait().type != pygame.QUIT: pass
            RUN = False
        pygame.display.flip()
        cloc.tick(60)
        key = pygame.key.get_pressed()
        if (key[pygame.K_w] or key[pygame.K_UP]) and dy != 1 and moved:
            dx, dy = 0, -1
            moved = False
        elif (key[pygame.K_s] or key[pygame.K_DOWN]) and dy != -1 and moved:
            dx, dy = 0, 1
            moved = False
        elif (key[pygame.K_a] or key[pygame.K_LEFT]) and dx != 1 and moved:
            dx, dy = -1, 0
            moved = False
        elif (key[pygame.K_d] or key[pygame.K_RIGHT]) and dx != -1 and moved:
            dx, dy = 1, 0
            moved = False


if __name__ == '__main__':
    run_snake()
    pygame.quit()
