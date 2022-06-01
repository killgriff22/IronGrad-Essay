import pygame,os
pygame.init()
pygame.mixer.init()
def loadassets():
    class assets:
        sprites=[]
        font=[]
        tmp=[]
        for NA,dirs,files in os.walk("./resources/"):
            for name in files:
                if "ICON.png" in name:
                    ICON=pygame.image.load(f"./resources/{name}")
                if (not "ICON.png" in name)and(not ".font" in name) and (".png" in name):
                    sprites.append([pygame.image.load(f"./resources/sprites/{name}"),f"{name.split('.png')[0]}"])
                if ".font.png" in name:
                    font.append([pygame.image.load(f"./resources/font/{name}"),(name.split('.font.png')[0])])
    return assets