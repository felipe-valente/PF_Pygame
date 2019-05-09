import pygame as pg
import random
from config import *
from Sprites import *


class Game:
	def __init__(self):
		pg.init()
		pg.mixer.init()
		self.screen = pg.display.set_mode((WIDTH,HEIGHT))
		pg.display.set_caption("Ship lander")
		self.clock = pg.time.Clock()
		self.rodando = True


	def new(self):
		self.all_sprites = pg.sprite.Group()
		self.player = Player()
		self.all_sprites.add(self.player)
		self.run()



	def run(self):
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
		self.all_sprites.draw(self.screen)

		pg.display.flip()



	def show_start_screen(self):
		pass


g = Game()
g.show_start_screen()
while g.rodando:
	g.new()
	g.show_go_screen

pg.quit()
