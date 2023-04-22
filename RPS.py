import pygame
import random
pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("game")
pygame.mixer.music.load("music.mp3")
background_image = pygame.image.load("background.png")


FPS = 60
clock = pygame.time.Clock()

VELOCITY = 2
scissors_image = pygame.image.load("Scissors.png")
scissors_rect = scissors_image.get_rect()
scissors_rect.x = random.randint(0, 300)
scissors_rect.y = random.randint(0, 300)
paper_image = pygame.image.load("Paper.png")
paper_rect = paper_image.get_rect()
paper_rect.x = random.randint(0, 500)
paper_rect.y = random.randint(0, 500)
stone_image = pygame.image.load("Stone.png")
stone_rect = stone_image.get_rect()
stone_rect.x = random.randint(0, 300)
stone_rect.y = random.randint(0, 300)
dx = random.randint(1, 2)
dy = random.randint(1, 2)
a = random.randint(1, 2)
b = random.randint(1, 2)
c = random.randint(1, 2)
d = random.randint(1, 2)
pygame.mixer.music.play(-1)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if paper_rect.left < 0 or paper_rect.right > WINDOW_WIDTH:
        dx = -dx
    if paper_rect.top < 0 or paper_rect.bottom > WINDOW_HEIGHT:
        dy = -dy
    if stone_rect.left < 0 or stone_rect.right > WINDOW_WIDTH:
        a = -a
    if stone_rect.top < 0 or stone_rect.bottom > WINDOW_HEIGHT:
        b = -b 
    if scissors_rect.left < 0 or scissors_rect.right > WINDOW_WIDTH:
        c = -c
    if scissors_rect.top < 0 or scissors_rect.bottom > WINDOW_HEIGHT:
        d = -d

    paper_rect.x += dx * VELOCITY
    paper_rect.y += dy * VELOCITY  
    stone_rect.x += a * VELOCITY 
    stone_rect.y += b * VELOCITY
    scissors_rect.x += c * VELOCITY 
    scissors_rect.y += d * VELOCITY
     
    if scissors_rect.colliderect(paper_rect):
        paper_rect = scissors_rect.copy()
        paper_rect.x = random.randint(0, 500)
        paper_rect.y = random.randint(0, 500)
    if stone_rect.colliderect(scissors_rect):
        scissors_rect = stone_rect.copy()
        scissors_rect.x = random.randint(0, 500)
        scissors_rect.y = random.randint(0, 500) 
    if paper_rect.colliderect(stone_rect):
        stone_rect = paper_rect.copy()
        stone_rect.x = random.randint(0, 500)
        stone_rect.y = random.randint(0, 500)   
    # if scissors_rect.colliderect(paper_rect):
    #     paper_rect = scissors_rect.copy()
        
    # if stone_rect.colliderect(scissors_rect):
    #     scissors_rect = stone_rect.copy()
        
    # if paper_rect.colliderect(stone_rect):
    #     stone_rect = paper_rect.copy()
           
  
    display_surface.fill((0, 0, 0))
    pygame.draw.rect(display_surface, (0, 255, 0), scissors_rect, 1)
    pygame.draw.rect(display_surface, (255, 0, 0), stone_rect, 1)
    pygame.draw.rect(display_surface, (0, 0, 255), paper_rect, 1)
    display_surface.blit(background_image, (0, 0))
    display_surface.blit(scissors_image, scissors_rect)
    display_surface.blit(stone_image, stone_rect)
    display_surface.blit(paper_image, paper_rect)
    
    pygame.display.update()
    clock.tick(FPS)
pygame.mixer.music.stop()
pygame.quit()