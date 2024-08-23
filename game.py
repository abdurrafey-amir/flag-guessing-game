import pygame


WIDTH = 800
HEIGHT = 600


# general setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Guess the Flag')
clock = pygame.time.Clock()



options = ['', '', '', '']

def show_options():
    for col in range(2):
        for row in range(2):
            rect = pygame.Rect(col * 350 + 100, 380 + row * 120, 250, 80)
            pygame.draw.rect(screen, (255, 255, 255), rect, 2)


# other rects
flagbox_rect = pygame.FRect(50, 50, 700, 300)
flag_surf = pygame.image.load('flag.png').convert_alpha()
# flag_surf = pygame.transform.scale(flag_surf, (660, 260))
flag_rect = flag_surf.get_frect(center=(WIDTH / 2, HEIGHT / 2))


# colors
grey = pygame.Color('grey12')





# main loop
running = True
while running:

    clock.tick(60)

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    
    screen.fill(grey)
    show_options()
    pygame.draw.rect(screen, (255, 255, 255), flagbox_rect, 2)
    screen.blit(flag_surf, flag_rect)


    pygame.display.flip()

pygame.quit()