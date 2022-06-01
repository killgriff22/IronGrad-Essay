
import pygame,assetloader
WIDTH = 360
HEIGHT = 480
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("IronGrad")
running = True
assets = assetloader.loadassets()
print((assets.sprites))
if assets.ICON:
    pygame.display.set_icon(assets.ICON)
def drawcell(x, y,tile:(pygame.surface.Surface)):
    screen.blit(tile,(x,y))
while 1:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill((0xFF,0xFF,0xFF))
        drawcell(10,10,assets.sprites[0][0])
        pygame.display.flip() 
    except KeyboardInterrupt:
        pygame.quit()      
