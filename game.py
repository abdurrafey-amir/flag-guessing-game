import pygame
import random
from flag import *
import os


WIDTH = 800
HEIGHT = 600

country_names, country_codes = get_countries()

def get_flag():
    country = random.choice(country_codes)
    flag = requests.get(f'https://flagcdn.com/256x192/{country}.png')

    with open('flag.png', 'wb') as f:
        f.write(flag.content)



# general setup
get_flag()
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Guess the Flag')
clock = pygame.time.Clock()




# other rects
flagbox_rect = pygame.FRect(50, 50, 700, 300)
flag_surf = pygame.image.load('flag.png').convert_alpha()
flag_surf = pygame.transform.scale(flag_surf, (600, 260))
flag_rect = flag_surf.get_frect(center=(WIDTH/2, 200))


font = pygame.font.Font('freesansbold.ttf', 32)

# colors
grey = pygame.Color('grey12')



# print(country_names)
options = country_names
rects = []

def show_options():
    for col in range(2):
        for row in range(2):
            rect = pygame.Rect(col * 350 + 100, 380 + row * 120, 250, 80)
            rects.append(rect)
            text = font.render(options[col * 2 + row], True, (255, 255, 255))
            screen.blit(text, (rect.x + 20, rect.y + 20))
            pygame.draw.rect(screen, (255, 255, 255), rect, 2)




# main loop
running = True
while running:

    clock.tick(60)
    
    
    
    screen.fill(grey)
    show_options()
    pygame.draw.rect(screen, (255, 255, 255), flagbox_rect, 2)
    screen.blit(flag_surf, flag_rect)
    
    
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            for rect in rects:
                if rect.collidepoint(event.pos):
                    pygame.draw.rect(screen, (255, 0, 0), rect, 2)
                    print('test')
                else:
                    pygame.draw.rect(screen, (255, 255, 255), rect, 2)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, rect in enumerate(rects):
                if rect.collidepoint(event.pos):
                    if options[i] == country_names[i]:
                        print("Correct!")
                    else:
                        print("Wrong!")
                        
                    get_flag()
                    show_options()
                    flag_surf = pygame.image.load('flag.png').convert_alpha()
                    flag_surf = pygame.transform.scale(flag_surf, (600, 260))
                    flag_rect = flag_surf.get_frect(center=(WIDTH/2, 200))
                    options = country_names
                    rects = []
                    
                    break


    pygame.display.flip()

pygame.quit()
os.remove('flag.png')