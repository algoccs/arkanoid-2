import pygame
pygame.init()

# Parametros
ANCHO, ALTO = 500, 500
COLOR_FONDO = (54, 74, 224)

# Pantalla (display)
screen = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

# Clase principal
class GameSprite():
    def __init__(self, file_img, x, y, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.image = pygame.transform.scale(pygame.image.load(file_img), (self.ancho, self.alto))
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

# Objetos (instancias)
player = GameSprite('pacman.png', 200, 400, 50, 50)
ball = 'no tengo'

# ENEMIGOS
enemy_x, enemy_y = 5, 5
count = 9
monsters = [] # Lista vacia, para llenarla de objetos (enemigos)

for i in range(3):
    y = (55 * i) + enemy_y
    x = (27.5 * i) + enemy_x
    for e in range(count):
        enemy = GameSprite('ghost.png', x, y, 50, 50)
        monsters.append(enemy)
        x += 55
    count -= 1

# Ciclo de juego
run = True
while run:
    screen.fill(COLOR_FONDO)
    player.draw() # DIBUJA A PLAYER
    for enemy in monsters:
        enemy.draw()

    pygame.display.update()
    reloj.tick(60)

pygame.quit()

