import pygame
import random
from config import *




pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Ship lander")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
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
	#atualiza tela para o sprite
	all_sprites.update()
	
	screen.fill(preto)
	all_sprites.draw(screen)

	pygame.display.flip()

pygame.quit()
