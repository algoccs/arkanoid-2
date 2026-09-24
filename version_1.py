import pygame

pygame.init()

# Constantes
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
BACKGROUND = (241, 120, 203)

vel_pelota_x = 5
vel_pelota_y = 5


class GameSprite():
    def __init__(self, sprite_image, x_pos, y_pos, sprite_width, sprite_height):
        self.width = sprite_width
        self.height = sprite_height
        self.image = pygame.transform.scale(pygame.image.load(sprite_image), (self.width, self.height))
        self.rect = pygame.Rect(x_pos, y_pos, sprite_width, sprite_height)
        self.rect.x = x_pos
        self.rect.y = y_pos

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    # Metodo que nos permite establecer colisiones entre objetos
    def collidepoint(self, x_pos, y_pos):
        return self.rect.collidepoint(x_pos, y_pos)
    
    def colliderect(self, rect):
        return self.rect.colliderect(rect)


# Main screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Arkanoid')


# Objetos
player = GameSprite('player.png', 200, 400, 104, 25)
ball = GameSprite('ball.png', 200, 370, 30, 30)

# Creacion de enemigos
enemy_x, enemy_y = 10, 5
count = 9
monsters = []

for i in range(3):
    y = (55 * i) + enemy_y
    x = (27.5 *i) + enemy_x

    for enemy in range(count):
        enemy = GameSprite('enemy.png', x, y, 40, 40)
        monsters.append(enemy)
        x += 55
    count -= 1
        
# Game Loop
clock = pygame.time.Clock()
running = True
finish = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    
    
    if not finish:
        screen.fill(BACKGROUND)
        for monster in monsters:
            monster.draw()
            
        player.draw()
        ball.draw()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
