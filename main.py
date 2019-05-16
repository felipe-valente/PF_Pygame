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
		self.font_name = pg.font.match_font(FONT_NAME)



	def new(self):
		self.all_sprites = pg.sprite.Group()
		self.platforms = pg.sprite.Group()
		self.player = Player()
		self.all_sprites.add(self.player)
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
			if hits[0].rect.top:
				self.jogando = False
				self.rodando = False

	def events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				if self.jogando:
					self.jogando = False
			self.rodando = False


		pass

	def draw(self):
		self.screen.fill(pfcolor)
		self.all_sprites.draw(self.screen)
		self.draw_text(str(self.player.fuel), 22, branco, WIDTH/2 , 15)

		pg.display.flip()



	def show_start_screen(self):
		self.screen.fill(pfcolor)
		self.draw_text(TITLE, 48, azulaleatorio, WIDTH/2, HEIGHT/4)
		self.draw_text("Use as setas para se movimentar!", 22, branco, WIDTH/2, HEIGHT/2)
		self.draw_text("Aperte qualquer botão para iniciar", 22, preto, WIDTH/2, HEIGHT*3/4)
		pg.display.flip()
		self.espera_por_tecla()


	def show_go_screen(self):
		self.screen.fill(preto)
		self.draw_text("GAME OVER", 78, vermelho, WIDTH/2, HEIGHT/4)
		self.draw_text("VOCÊ É GAY BRO!", 50, branco, WIDTH/2, HEIGHT/2)
		self.draw_text("RAFA MOREIRA! GANG GANG GANG!! 777", 37, branco, WIDTH/2, HEIGHT*3/4)
		pg.display.flip()
		self.espera_por_tecla()

	def espera_por_tecla(self):
		esperando = True
		while esperando:
			self.clock.tick(FPS)
			for event in pg.event.get():
				if event.type == pg.QUIT:
					esperando = False
					self.running = False
				if event.type == pg.KEYUP:
					esperando = False

	def draw_text(self, text, size, color, x, y):
		font = pg.font.Font(self.font_name, size)
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect()
		text_rect.midtop = (x,y)
		self.screen.blit(text_surface, text_rect)


g = Game()
g.show_start_screen()
while g.rodando:
	g.new()

g.show_go_screen()
pg.quit()
