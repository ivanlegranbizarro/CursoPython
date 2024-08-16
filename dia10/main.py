import pygame
import random

# Iniciar Pygame
pygame.init()

# Crear la pantalla del juego
pantalla = pygame.display.set_mode((800, 600))
ejecutandose = True

# Variables del jugador
nave_jugador = pygame.image.load("spaceship.png")
x_jugador = 368
y_jugador = 536
x_cambio_jugador = 0
y_cambio_jugador = 0

# Variables del enemigo
nave_enemigo = pygame.image.load("enemigo.png")
x_enemigo = random.randint(0, 736)
y_enemigo = random.randint(50, 200)
x_cambio_enemigo = 0
y_cambio_enemigo = 0


# Función para invocar la aparición del jugador
def jugador(x, y):
    pantalla.blit(nave_jugador, (x, y))


# Función para invocar la aparición del enemigo
def enemigo(x, y):
    pantalla.blit(nave_enemigo, (x, y))


# Título e icono
pygame.display.set_caption("Invasión Espacial")
icono_ovni = pygame.image.load("ovni.png")
pygame.display.set_icon(icono_ovni)

# Loop de ejecución del juego
while ejecutandose:

    # Color RGB de la pantalla del juego
    pantalla.fill((205, 144, 228))

    # Iterar por todos los eventos
    for evento in pygame.event.get():
        # Si el evento es cerrar la ventana el juego termina
        if evento.type == pygame.QUIT:
            ejecutandose = False

        # Movimiento del jugador si se presiona una tecla
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                x_cambio_jugador -= 0.3
            if evento.key == pygame.K_RIGHT:
                x_cambio_jugador += 0.3
        # Movimiento del jugador si se deja de presionar una tecla
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                x_cambio_jugador = 0

    # Modificar la ubicación del jugador
    x_jugador += x_cambio_jugador

    # Mantener el jugador dentro de la pantalla
    if x_jugador <= 0:
        x_jugador = 0
    elif x_jugador >= 736:
        x_jugador = 736

    # Invocamos la aparición de la nave del jugador y la de las naves enemigas
    jugador(x_jugador, y_jugador)
    enemigo(x_enemigo, y_enemigo)

    # Actualizar la pantalla
    pygame.display.update()
