# Импорт pygame
# Импорт random
import time

import pygame
import random
# Высота и ширина игрового экрана
WIDTH, HEIGHT = 1200, 700
FPS = 60
# Свойства ракетка (w, h, speed, color, dx, dy)
paddle_w = 330
paddle_h = 35
paddle_speed = 15
paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h)

# Свойства шарика
ball_radius = 20
ball_speed = 6
ball_rect = int(ball_radius * 2 ** 1/2)
dx, dy = 1, -1
ball = pygame.Rect(random.randrange(ball_rect, WIDTH-ball_rect), HEIGHT//2, ball_rect, ball_rect)

# Создать блоки
block_list = []
for i in range(10):
    for k in range(4):
       block_list.append( pygame.Rect(10 + 120 * i, 10 +70*k, 100, 50) )

# Описать функцию столкновений
def collision(dx, dy, ball, rect):
    if dx > 0:
        deltaX = ball.right - rect.left
    else:
        deltaX = rect.right - ball.left

    if dy > 0:
        deltaY = ball.bottom - rect.top
    else:
        deltaY = rect.bottom - ball.top

    if abs(deltaX - deltaY) < 10:
        dx = -dx
        dy = -dy
    elif deltaX > deltaY:
        dy = -dy
    elif deltaY > deltaX:
        dx = -dx
    return dx, dy


#  Запускаем pygame (while True:)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()

img = pygame.image.load("1.jpg").convert()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(img, (0,0))

    # Рисуем блоки
    for block in block_list:
        pygame.draw.rect(screen, pygame.Color("pink"), block)

    # Рисуем ракетку
    pygame.draw.rect(screen, pygame.Color("red"), paddle)
    # Рисуем шарик
    pygame.draw.circle(screen, pygame.Color("white"), ball.center, ball_radius)
    # Рисовать движение шарика
    ball.x = ball.x + ball_speed * dx
    ball.y = ball.y + ball_speed * dy

    # Шарик отбивается от стенок
    if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
        dx = -dx

    if ball.centery < ball_radius or ball.centery > HEIGHT - ball_radius:
        dy = -dy

    # Столкновение с ракеткой
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = collision(dx, dy, ball, paddle)

    # Движения ракетки
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left = paddle.left - paddle_speed
    if key[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right = paddle.right + paddle_speed

    # Столкновени с блоками
    hit = ball.collidelist(block_list)
    if hit != -1:
        hit_rect = block_list.pop(hit)
        dx, dy = collision(dx, dy, ball, hit_rect)
        FPS += 1

    # Условие Game Over
    if ball.bottom >= HEIGHT - ball_radius:
        print("Game Over")
        time.sleep(2)
        exit()
    # Условие WIN
    elif len(block_list) == 0:
        print("Win !!!")
        time.sleep(2)
        exit()



    pygame.display.flip()
    timer.tick(FPS)

