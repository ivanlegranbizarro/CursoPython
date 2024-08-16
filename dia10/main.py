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
x_cambio_jugador = 0
y_cambio_jugador = 0


def jugador(x, y):
    pantalla.blit(nave_jugador, (x, y))


# Título e icono
pygame.display.set_caption("Invasión Espacial")
icono_ovni = pygame.image.load("ovni.png")
pygame.display.set_icon(icono_ovni)

# Loop de ejecución del juego
while ejecutandose:

    # Color RGB de la pantalla del juego
    pantalla.fill((205, 144, 228))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutandose = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                x_cambio_jugador -= 0.1
            if evento.key == pygame.K_RIGHT:
                x_cambio_jugador += 0.1
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                x_cambio_jugador = 0

    # Invocamos la aparición de la nave del jugador
    x_jugador += x_cambio_jugador
    jugador(x_jugador, y_jugador)
    pygame.display.update()
