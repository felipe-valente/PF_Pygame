import pygame as pg
import random
from config import *


class Game:
	def __init__(self):
		pg.init()
		pg.mixer.init()
		screen = pg.display.set_mode((WIDTH,HEIGHT))
		pg.display.set_caption("Ship lander")
		clock = pg.time.Clock()
		self.rodando = True
		

	def new(self):
		self.all_sprites = pg.sprite.Group()
		self.run()
		


	def roda(self):
		self.jogando = True
		while self.jogando:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw() 


	def update(self):
		self.all_sprites.update()

	def events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				if self.jogando:
					self.jogando = False
			self.rodando = False

		pass

	def draw(self):
		self.screen.fill(preto)
		self.all_sprites.draw(screen)

		pg.display.flip()

		

	def show_start_screen(self):
		pass


g = Game()
g.show_start_screen()
while g.rodando:
	g.new()
	g.show_go_screen

pg.quit()




