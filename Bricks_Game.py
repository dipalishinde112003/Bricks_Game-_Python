import pygame

# Initialize module
pygame.init()

WHITE = (255, 255, 255)
DARKBLUE = (36, 90, 190)
LLIGHTBLUE = (0, 176, 240)
RED = (255, 0, 0)

# BRICKS
bricks1 = [pygame.Rect(10 + i * 100, 60, 80, 30) for i in range(7)]
bricks2 = [pygame.Rect(10 + i * 100, 100, 80, 30) for i in range(6)]
bricks3 = [pygame.Rect(10 + i * 100, 140, 80, 30) for i in range(6)]

# bricks draw on screen
def draw(bricks):
    for i in bricks:
        pygame.draw.rect(screen, RED, i)

score = 0
velocity = [1, 1]
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bricks Game")

paddle = pygame.Rect(270, 550, 200, 10)  # Adjusted paddle width
ball = pygame.Rect(50, 250, 10, 10)

gameCon = True
while gameCon:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameCon = False

    # paddle move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if paddle.x < 540:
            paddle.x += 5
    if keys[pygame.K_LEFT]:
        if paddle.x > 0:
            paddle.x -= 5

    screen.fill(DARKBLUE)
    pygame.draw.rect(screen, LLIGHTBLUE, paddle)
    font = pygame.font.Font(None, 34)
    text = font.render("SCORE" + str(score), 1, WHITE)
    screen.blit(text, (20, 10))

    draw(bricks1)
    draw(bricks2)
    draw(bricks3)

    # ball movement
    ball.x += velocity[0]
    ball.y += velocity[1]

    if ball.x > 590 or ball.x < 0:
        velocity[0] = -velocity[0]
    if ball.y < 0:
        velocity[1] = -velocity[1]
    if paddle.collidepoint(ball.x, ball.y):
        velocity[1] = -velocity[1]
    if ball.y >= 590:
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", 1, RED)
        screen.blit(text, (150, 350))
        pygame.display.flip()
        pygame.time.wait(2000)
        break

    pygame.draw.rect(screen, WHITE, ball)
    
    for i in bricks1:
        if i.collidepoint(ball.x, ball.y):
            bricks1.remove(i)
            velocity[0] = -velocity[0]
            velocity[1] = -velocity[1]
            score += 1
    for i in bricks2:
        if i.collidepoint(ball.x, ball.y):
            bricks2.remove(i)
            velocity[0] = -velocity[0]
            velocity[1] = -velocity[1]
            score += 1
    for i in bricks3:
        if i.collidepoint(ball.x, ball.y):
            bricks3.remove(i)
            velocity[0] = -velocity[0]
            velocity[1] = -velocity[1]
            score += 1

    if score == 18:
        font = pygame.font.Font(None, 74)
        text = font.render("YOU WON", 1, RED)
        screen.blit(text, (150, 350))
        pygame.display.flip()
        pygame.time.wait(3000)
        break

    pygame.time.wait(1)
    pygame.display.flip()

pygame.quit()
