import pygame

# Iniciar Pygame
pygame.init()

# Crear la pantalla del juego
pantalla = pygame.display.set_mode((800, 600))
ejecutandose = True

# Titulo e icono
pygame.display.set_caption("Invasión Espacial")
icono_ovni = pygame.image.load("ovni.png")
pygame.display.set_icon(icono_ovni)

# Loop de ejecución del juego
while ejecutandose:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutandose = False

    pantalla.fill((205, 144, 228))
    pygame.display.update()
