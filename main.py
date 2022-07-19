
import pygame,assetloader
tilesize=50
WIDTH = tilesize*20
HEIGHT = tilesize*10
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("IronGrad")
running = True
assets = assetloader.loadassets()
print((assets.sprites))
if assets.ICON:
    pygame.display.set_icon(assets.ICON)
def drawcell(x:int, y:int,tile:(pygame.surface.Surface)) -> None:
    screen.blit(tile,(x,y))
map = [[[]*30]*30]
while 1:
    try:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if x%tilesize==0:
                    screen.set_at((x,y),(0,0,0))
                if y%tilesize==0:
                    screen.set_at((x,y),(0,0,0))
                if x%tilesize==0 and y%tilesize==0:
                    screen.blit(pygame.transform.scale(assets.sprites[0][0],(tilesize,tilesize)),(x,y))
        pygame.display.flip() 
    except KeyboardInterrupt or pygame.error:
        pygame.quit()      
