import pygame
import random


WIDTH = 360
HEIGHT = 480
FPS = 100

preto = (0,0,0)
branco = (255,255,255)
azul = (0,0,255)
vermelho = (255,0,0)
verde = (0,255,0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Ship lander")
clock = pygame.time.Clock()

#Game loop
rodando = True
while rodando:
	#deixa o loop rodadando na velocidade certa
	clock.tick(FPS)
	#processos de inputs/eventos
	for event in pygame.event.get():
		#fecha o jogo no "X"
		if event.type == pygame.QUIT:
			rodando = False

	screen.fill(preto)
	pygame.display.flip()

pygame.quit()
