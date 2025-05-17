import pygame
pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("match the picture")
pygame.font.init()

# Load images
candy = pygame.image.load("images/candy crush.jpg")

screen.blit(candy, (50,50))
text1 = pygame.font.SysFont('comicsans', 40).render("candy crush", 1, (255, 255, 255))
screen.blit(text1, (550,350))


ludo = pygame.image.load("images/ludo.png")

screen.blit(ludo, (50,150))
text2 = pygame.font.SysFont('comicsans', 40).render("ludo", 1, (255, 255, 255))
screen.blit(text2, (550,50))


subway_surfer = pygame.image.load("images/subway surfer.png")

screen.blit(subway_surfer, (50,250))
text3 = pygame.font.SysFont('comicsans', 40).render("subway surfer", 1, (255, 255, 255))
screen.blit(text3, (550,250))


temple_run = pygame.image.load("images/temple run.png")

screen.blit(temple_run, (50,350))
text4 = pygame.font.SysFont('comicsans', 40).render("temple run", 1, (255, 255, 255))
screen.blit(text4, (550,150))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
     
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen,(255,255,255),pos,20)
        pygame.display.update()
    
    elif event.type == pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        pygame.draw.line(screen,(255,255,255),pos,pos2,5)
        pygame.draw.circle(screen,(255,255,255),pos2,20)
        pygame.display.update()

