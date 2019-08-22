import pygame
window_width = 490
window_height = 500
win = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption(("Space Invaders?"))

class bar(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 7

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.width, self.height), 0)

class projectile(object):
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.vel = 10
        self.color = color
        self.radius = radius
        self.hasHit = False

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def hits(self, block_x, block_y, block_width):
        if  (self.x > block_x) and (self.x < (block_x + block_width)) and (self.y < (block_y + block_width)):
            self.hasHit = True

class block(object):
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.height = width
        self.isBroken = False

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.width, self.height), 0)

    def isCollided(self, projectile_x, projectile_y):
        if (projectile_x > self.x) and (projectile_x < (self.x + self.width)) and (projectile_y < (self.y + self.height)):
            self.isBroken= True

#Updates the screen
def redrawGameWindow():
    win.fill((0,0,0))
    bar.draw(win)
    for bullet in bullets:
        if bullet.hasHit == False:
            bullet.draw(win)

    for block in blocks:
        if block.isBroken == False:
            block.draw(win)
        else:
            blocks.pop(blocks.index(block))

    pygame.display.update()

run = True
bar = bar(500/2, 450, 50 , 10)
#Initializes
bullets = []

#Initializes block array
blocks = []
for y in range(3):
    for x in range(8):
        blocks.append(block((10*(x+1)+(50*x)), (10*(y+1)+(50*y)), 50))

#main loop
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#check for hits or going out of screen
    for bullet in bullets:
        if (bullet.hasHit == False) and (bullet.y > 0):
            bullet.y -= bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
#bar movement
    if keys[pygame.K_a] and bar.x > 0 :
        bar.x -= bar.vel
    elif keys[pygame.K_d] and bar.x < (window_width - bar.width):
        bar.x += bar.vel

    if keys[pygame.K_SPACE]:
        if len(bullets) < 1:
            bullets.append(projectile(round(bar.x+(bar.width//2)), bar.y, (255, 255, 255), 5))

    for bullet in bullets:
        for block in blocks:
            block.isCollided(bullet.x, bullet.y)
            bullet.hits(block.x, block.y, block.width)

    redrawGameWindow()

pygame.quit()
