import math
import random

import pygame
from pygame import mixer

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
nave_enemigo = []
x_enemigo = []
y_enemigo = []
x_cambio_enemigo = []
y_cambio_enemigo = []
cantidad_enemigos = 8

for _ in range(cantidad_enemigos):
    nave_enemigo.append(pygame.image.load("enemigo.png"))
    x_enemigo.append(random.randint(0, 736))
    y_enemigo.append(random.randint(50, 200))
    x_cambio_enemigo.append(0.3)
    y_cambio_enemigo.append(40)

# Variables de la bala
bala = pygame.image.load("bala.png")
x_bala = 0
y_bala = 500
x_cambio_bala = 0
y_cambio_bala = 1
bala_visible = False

# Puntuación
puntuacion = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)
coordenada_x_texto = 10
coordenada_y_texto = 10

# Texto de GameOver
fuente_game_over = pygame.font.Font("freesansbold.ttf", 64)


def texto_final():
    texto_final = fuente_game_over.render("GAME OVER", True, (255, 255, 255))
    pantalla.blit(texto_final, (200, 200))


# Mostrar puntuación
def mostrar_puntuacion(x, y):
    texto = fuente.render(f"Puntuación: {puntuacion}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# Función para invocar la aparición del jugador
def jugador(x, y):
    pantalla.blit(nave_jugador, (x, y))


# Función para invocar la aparición del enemigo
def enemigo(x, y, ene):
    pantalla.blit(nave_enemigo[ene], (x, y))


# Función para disparar la bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(bala, (x + 16, y + 10))


# Función para detectar las colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    return distancia < 27


# Título e icono
pygame.display.set_caption("Invasión Espacial")
icono_ovni = pygame.image.load("ovni.png")
pygame.display.set_icon(icono_ovni)
fondo = pygame.image.load("Fondo.jpg")

# Añadir música
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

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
                sonido_disparo = mixer.Sound("disparo.mp3")
                sonido_disparo.play()
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
    for i in range(cantidad_enemigos):
        # Fin del juego (si un enemigo choca con nuestra nave)
        if y_enemigo[i] > 500:
            for k in range(cantidad_enemigos):
                y_enemigo[k] = 1000
            texto_final()
            break

        x_enemigo[i] += x_cambio_enemigo[i]

        # Mantener el enemigo dentro de la pantalla
        if x_enemigo[i] <= 0:
            x_cambio_enemigo[i] = 0.3
            y_enemigo[i] += y_cambio_enemigo[i]
        elif x_enemigo[i] >= 736:
            x_cambio_enemigo[i] = -0.3
            y_enemigo[i] += y_cambio_enemigo[i]

        # Colisión
        colision = hay_colision(x_enemigo[i], y_enemigo[i], x_bala, y_bala)
        if colision:
            sonido_colision = mixer.Sound("Golpe.mp3")
            sonido_colision.play()
            y_bala = 500
            bala_visible = False
            puntuacion += 1
            # Reiniciar la posición del enemigo después de la colisión
            x_enemigo[i] = random.randint(0, 736)
            y_enemigo[i] = random.randint(50, 200)

        # Invocar la aparición del enemigo
        enemigo(x_enemigo[i], y_enemigo[i], i)

    # Movimiento bala
    if bala_visible:
        disparar_bala(x_bala, y_bala)
        y_bala -= y_cambio_bala

    # Verificar si la bala ha salido de la pantalla
    if y_bala <= 0:
        y_bala = 500
        bala_visible = False

    # Invocamos la aparición de la nave del jugador
    jugador(x_jugador, y_jugador)

    # Mostrar puntuación
    mostrar_puntuacion(coordenada_x_texto, coordenada_y_texto)

    # Actualizar la pantalla
    pygame.display.update()
