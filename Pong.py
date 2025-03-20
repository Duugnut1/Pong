import pygame
import random

pygame.init()

running = True

ball_dx = 0.25 * random.uniform(-1,-1)
ball_dy = 0.25 * random.uniform(-1, 1)
enemy_speed = 1
ball_x = 400
ball_y = 500
ball_rad = 20

font = pygame.font.Font(None, 36)
Bigfont = pygame.font.Font(None, 72)

wins = {}

screen = pygame.display.set_mode((1000, 800))
player = pygame.Rect(50, 400 ,10 ,150)
enemy = pygame.Rect(950, 400 ,10 ,150)
ball_rect = pygame.Rect(0, 0 ,40 ,40)

score = 0
best = 0
dead = False

def save(score, best):
    if score > best:
        best = score
    score = 0
    return score, best

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and dead:
                dead = False
                score = 0
                ball_x = 500
                ball_y = 400

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.y -= 1
    if keys[pygame.K_s]:
        player.y += 1
        
    if player.y <= 0:
        player.y = 0
    if player.y >= 650:
        player.y = 650
        
    enemy.y += enemy_speed
    
    if enemy.y <= 0:
        enemy_speed = random.randint(1, 3)
    elif enemy.y >= 650:
        enemy_speed = -random.randint(1, 3)
        
    ball_x += ball_dx
    ball_y += ball_dy
    
    ball_rect.x = ball_x - ball_rad
    ball_rect.y = ball_y - ball_rad
        
    if ball_y - ball_rad <= 0 or ball_y + ball_rad >= 800:
        ball_dy = -ball_dy

    if ball_x - ball_rad <= 40:
        dead = True
        score, best = save(score, best)
        ball_dx = -0.25 * random.uniform(-1,-1)
        ball_dy = -0.25 * random.uniform(-1, 1)

    elif ball_x + ball_rad >= 960:
        score += 1
        ball_x = 500
        ball_y = 400
        ball_dx = 0.25 * random.uniform(-1,-1)
        ball_dy = 0.25 * random.uniform(-1, 1)
    
    if ball_rect.colliderect(player) or ball_rect.colliderect(enemy):
        ball_dx = -ball_dx
       
    screen.fill((0, 0, 0)) 
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.draw.rect(screen, (255, 255, 255), enemy)
    pygame.draw.circle(screen, (255, 255, 255), (int(ball_x), int(ball_y)), ball_rad)
    score_text = font.render("score:" + str(score), True, (255, 255, 255))
    screen.blit(score_text, (450, 10))
    
    dead_text = Bigfont.render("FUCK YOU BITCH YOU DIED", True, (255, 0, 0))
    restart_text = font.render("'r' to restart", True, (255, 255, 255))
    best_text = font.render("Best Score:" + str(best), True, (255, 255, 255))
    
    if dead:
        ball_x = 500
        ball_y = 400
        enemy.y = 400
        screen.blit(dead_text, (200, 300))
        screen.blit(restart_text, (300, 400))
        screen.blit(best_text, (300, 450))
    
    pygame.display.update()