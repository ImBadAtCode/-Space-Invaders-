import pygame

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption(("Brick Breaker"))

class bar():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 7

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.width, self.height), 0)

class ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self,win):
        pygame.draw.circle(win,(255,255,255), (self.x, self.y), 5)

class block():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def redrawGameWindow():
    win.fill((0,0,0))
    bar.draw(win)
    pygame.display.update()

run = True
bar = bar(500/2, 450, 50 , 10)


while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and bar.x > 0 :
        bar.x -= bar.vel
    elif keys[pygame.K_d] and bar.x < (500 - bar.width):
        bar.x += bar.vel

    redrawGameWindow()

pygame.quit()
