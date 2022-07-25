import pygame,assetloader,random
tilesize=50
tilecountx, tilecounty= 20,10
WIDTH = tilesize*tilecountx
HEIGHT = tilesize*tilecounty
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("IronGrad")
assets = assetloader.loadassets()
if assets.ICON:
    pygame.display.set_icon(assets.ICON)
def drawcell(x:int, y:int,tile:(pygame.surface.Surface)) -> None:
    screen.blit(tile,(x,y))
grasstypes=["wheat","grass","grass"]
map = [[[f"grass-{random.choice(grasstypes)}"]]*tilecountx]*tilecounty
print(len(map),len(map[0]))
while 1:
    try:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if x%tilesize == 0:
                   screen.set_at((x, y),(0, 0, 0))
                   screen.set_at((x+1, y),(0, 0, 0))
                if y%tilesize == 0:
                    screen.set_at((x, y),(255, 0, 0))
                    screen.set_at((x, y+1),(255, 0, 0))
        pygame.display.update()
    except KeyboardInterrupt or pygame.error:
        pygame.quit()      
