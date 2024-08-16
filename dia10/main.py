import math
import random

import pygame

# Fórmula para las colisiones= Distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Iniciar Pygame
pygame.init()

# Crear la pantalla del juego
pantalla = pygame.display.set_mode((800, 600))
ejecutandose = True

# Variables del jugador
nave_jugador = pygame.image.load("spaceship.png")
x_jugador = 368
y_jugador = 500
x_cambio_jugador = 0

# Variables del enemigo
nave_enemigo = pygame.image.load("enemigo.png")
x_enemigo = random.randint(0, 736)
y_enemigo = random.randint(50, 200)
x_cambio_enemigo = 0.3
y_cambio_enemigo = 40

# Variables de la bala
bala = pygame.image.load("bala.png")
x_bala = 0
y_bala = 500
x_cambio_bala = 0
y_cambio_bala = 1
bala_visible = False

# Puntuación
puntuacion = 0


# Función para invocar la aparición del jugador
def jugador(x, y):
    pantalla.blit(nave_jugador, (x, y))


# Función para invocar la aparición del enemigo
def enemigo(x, y):
    pantalla.blit(nave_enemigo, (x, y))


# Función para disparar la bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(bala, (x + 16, y + 10))


# Función para detectar las colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    return False


# Título e icono
pygame.display.set_caption("Invasión Espacial")
icono_ovni = pygame.image.load("ovni.png")
pygame.display.set_icon(icono_ovni)
fondo = pygame.image.load("Fondo.jpg")

# Loop de ejecución del juego
while ejecutandose:

    # Cargar la imagen de fondo
    pantalla.blit(fondo, (0, 0))

    # Iterar por todos los eventos
    for evento in pygame.event.get():
        # Si el evento es cerrar la ventana el juego termina
        if evento.type == pygame.QUIT:
            ejecutandose = False

        # Movimiento del jugador si se presiona una tecla
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                x_cambio_jugador = -0.3
            if evento.key == pygame.K_RIGHT:
                x_cambio_jugador = 0.3

            # Disparar balas
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    x_bala = x_jugador
                    y_bala = y_jugador
                    disparar_bala(x_bala, y_bala)

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

    # Modificar la ubicación del enemigo
    x_enemigo += x_cambio_enemigo

    # Mantener el enemigo dentro de la pantalla
    if x_enemigo <= 0:
        x_cambio_enemigo = 0.3
        y_enemigo += y_cambio_enemigo
    elif x_enemigo >= 736:
        x_cambio_enemigo = -0.3
        y_enemigo += y_cambio_enemigo

    # Movimiento bala
    if bala_visible:
        disparar_bala(x_bala, y_bala)
        y_bala -= y_cambio_bala

    # Verificar si la bala ha salido de la pantalla
    if y_bala <= 0:
        y_bala = 500
        bala_visible = False

    # Colisión
    colision = hay_colision(x_enemigo, y_enemigo, x_bala, y_bala)
    if colision:
        y_bala = 500
        bala_visible = False
        puntuacion += 1
        print(puntuacion)
        # Reiniciar la posición del enemigo después de la colisión
        x_enemigo = random.randint(0, 736)
        y_enemigo = random.randint(50, 200)

    # Invocamos la aparición de la nave del jugador y la de las naves enemigas
    jugador(x_jugador, y_jugador)
    enemigo(x_enemigo, y_enemigo)

    # Actualizar la pantalla
    pygame.display.update()
