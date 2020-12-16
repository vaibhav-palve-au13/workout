import pygame
from random import randrange
pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 128, 0)

wid = hei = 500
screen = pygame.display.set_mode((wid, hei))
pygame.display.set_caption('Snake')
scoreboard = 40


def snake(snk_xy, size):
    for xy in snk_xy:
        pygame.draw.rect(screen, white, (xy[0], xy[1], size, size))


def apple(apl_x, apl_y, size):
    pygame.draw.rect(screen, green, (apl_x, apl_y, size, size))


def text(txt_msg, txt_clr, txt_x, txt_y, txt_size, ):
    font = pygame.font.SysFont('arial', txt_size)
    txt = font.render(txt_msg, True, txt_clr)
    screen.blit(txt, (txt_x, txt_y))


def game():
    main = True
    game_over = False
    clock = pygame.time.Clock()
    score = 0


    snk_x, snk_y = int(wid / 2), int(hei / 2)
    snk_xy = []
    snk_scale = 0
    size = 10
    spd_x = spd_y = 0
    apl_x = randrange(0, wid - size, size)
    apl_y = randrange(0, hei - size - scoreboard, size)

    while main:
        clock.tick(5)
        screen.fill(black)
        pygame.draw.rect(screen, white, (0, hei - scoreboard, wid, scoreboard))

        text('Score: ' + str(score), black, 10, wid - scoreboard, 20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and spd_y != size:
                    spd_x = 0
                    spd_y = - size
                if event.key == pygame.K_DOWN and spd_y != -size:
                    spd_x = 0
                    spd_y = size
                if event.key == pygame.K_RIGHT and spd_x != -size:
                    spd_y = 0
                    spd_x = size
                if event.key == pygame.K_LEFT and spd_x != size:
                    spd_y = 0
                    spd_x = - size

        snk_x += spd_x
        snk_y += spd_y

        if snk_x >= hei or snk_x < 0 or snk_y >= wid - scoreboard or snk_y < 0:
            game_over = True

        if snk_x == apl_x and snk_y == apl_y:
            apl_x = randrange(0, wid - size, size)
            apl_y = randrange(0, hei - size - scoreboard, size)
            snk_scale += 1
            score += 1

        if len(snk_xy) > snk_scale:
            del snk_xy[0]
        snk_head = [snk_x, snk_y]
        snk_xy.append(snk_head)

        if any(bloc == snk_head for bloc in snk_xy[: -1]):
            game_over = True

        snake(snk_xy, size)
        apple(apl_x, apl_y, size)

        pygame.display.update()

        while game_over:
            screen.fill(black)
            pygame.draw.rect(screen, white, (30, 130, 100, 25))
            pygame.draw.rect(screen, white, (195, 130, 60, 25))

            text('Game Over', white, 90, 60, 30)
            text('Score: ' + str(score), white, 10, wid - scoreboard, 20)
            text('Play Again', black, 30, 130, 20)
            text('No', black, 195, 130, 20)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    main = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        return game()
                    elif event.key == pygame.K_n:
                        game_over = False
                        main = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x = pygame.mouse.get_pos()[0]
                    mouse_y = pygame.mouse.get_pos()[1]
                    if 30 < mouse_x < 130 < mouse_y < 155:
                        return game()
                    if 195 < mouse_x < 255 and 130 < mouse_y < 155:
                        game_over = False
                        main = False

            pygame.display.update()


game()

pygame.quit()
