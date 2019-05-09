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
		self.platforms = pg.sprite.Group()
		self.player = Player()
		self.all_sprites.add(self.player)
		p1 = Platform(0, HEIGHT-40, WIDTH, 40)
		self.all_sprites.add(p1)
		self.platforms.add(p1)
		p2 = Platform(WIDTH/2 - 50, HEIGHT * 3/4, 100, 20)
		self.all_sprites.add(p2)
		self.platforms.add(p2)
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
		hits = pg.sprite.spritecollide(self.player, self.platforms, False)
		if hits:
			self.player.pos.y = hits[0].rect.top
			self.player.vel.y = 0

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
