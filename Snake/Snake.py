import pygame
import random

WINDOW = 400
GRID = 10

x = random.randrange(0, WINDOW, GRID)
y = random.randrange(0, WINDOW, GRID)

appleX = random.randrange(0, WINDOW, GRID)
appleY = random.randrange(0, WINDOW, GRID)

snake = [(x, y)]
dx, dy = 0, 0
fps = 5
score = 0
length = 1

pygame.init()
screen = pygame.display.set_mode([WINDOW, WINDOW])
surface = pygame.display.set_mode([WINDOW, WINDOW])
timer = pygame.time.Clock()

text_score = pygame.font.SysFont("Verdana", 20)
text_game_over = pygame.font.SysFont("Verdana", 40)



def game_over():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


while True:
    screen.fill("lightyellow")
    game_over()

    render_score = text_score.render(f"Яблоки : {score}", 1, pygame.Color("orange"))
    surface.blit(render_score, (250, 5))

    for i, j in snake:
        pygame.draw.rect(screen, "green", (i, j, GRID-3, GRID-3))

    pygame.draw.rect(screen, "red", (appleX, appleY, GRID, GRID))

    if snake[-1] == (appleX, appleY):  # (x,y) == (appleX, appleY)
        appleX = random.randrange(0, WINDOW, GRID)
        appleY = random.randrange(0, WINDOW, GRID)
        length += 1
        score += 1
        fps += 1
        if fps > 15:
            fps = 10
        else:
            fps +=1

    if x < 0 or x > WINDOW - GRID or y < 0 or y > WINDOW - GRID:
        text_game_over.render(f"GAME OVER - {score}ЯБЛОК",1,pygame.Color("red") )
        pygame.display.flip()
        game_over()

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        dy = -1
        dx = 0
    if key[pygame.K_s]:
        dy = 1
        dx = 0
    if key[pygame.K_a]:
        dy = 0
        dx = -1

    if key[pygame.K_d]:
        dy = 0
        dx = 1

    x = x + dx * GRID
    y = y + dy * GRID
    snake.append((x,y))
    snake = snake[-length:]

    pygame.display.flip()
    timer.tick(fps)
