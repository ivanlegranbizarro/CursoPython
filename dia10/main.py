import pygame

# Iniciar Pygame
pygame.init()

# Crear la pantalla del juego
pantalla = pygame.display.set_mode((800, 600))
ejecutandose = True

# Jugador
nave_jugador = pygame.image.load("spaceship.png")
x_jugador = 368
y_jugador = 536


def jugador():
    pantalla.blit(nave_jugador, (x_jugador, y_jugador))


# Título e icono
pygame.display.set_caption("Invasión Espacial")
icono_ovni = pygame.image.load("ovni.png")
pygame.display.set_icon(icono_ovni)

# Loop de ejecución del juego
while ejecutandose:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutandose = False

    # Color RGB de la pantalla del juego
    pantalla.fill((205, 144, 228))

    # Invocamos la aparición de la nave del jugador
    jugador()
    pygame.display.update()
