import pygame as pg
import random
from config import *
from Sprites import *


class Game:
	def __init__(self):
		pg.init()
		pg.mixer.init()
		pg.mixer.music.load("Mask_Off_8bit_bg.mp3")
		pg.mixer.music.play(-1)
		self.screen = pg.display.set_mode((WIDTH,HEIGHT))
		pg.display.set_caption("Ship lander")
		self.clock = pg.time.Clock()
		self.rodando = True
		self.font_name = pg.font.match_font(FONT_NAME)
		self.pouso = False


	def new(self):
		self.all_sprites = pg.sprite.Group()
		self.boundaries = pg.sprite.Group()
		self.power_up = pg.sprite.Group( )
		self.platforms = pg.sprite.Group()
		self.player = Player()
		self.all_sprites.add(self.player)
		b1 = Boundaries(WIDTH/4, 0, 20, HEIGHT * 3/4)
		self.all_sprites.add(b1)
		self.boundaries.add(b1)
		b2 = Boundaries(WIDTH/2, HEIGHT/4, 20, HEIGHT * 3/4)
		self.all_sprites.add(b2)
		self.boundaries.add(b2)
		b3 = Boundaries(WIDTH*3/4, 0, 20, HEIGHT * 3/4)
		self.all_sprites.add(b3)
		self.boundaries.add(b3)
		self.PU1 = PowerUp(WIDTH/8, HEIGHT/8)
		self.all_sprites.add(self.PU1)
		self.power_up.add(self.PU1)
		self.PU2 = PowerUp(WIDTH/4, HEIGHT*7/8)
		self.all_sprites.add(self.PU2)
		self.power_up.add(self.PU2)
		self.PU3 = PowerUp(WIDTH/2, HEIGHT/8)
		self.all_sprites.add(self.PU3)
		self.power_up.add(self.PU3)
		self.run()

	def new_2(self):
		self.all_sprites = pg.sprite.Group()
		self.boundaries = pg.sprite.Group()
		self.power_up = pg.sprite.Group( )
		self.platforms = pg.sprite.Group()
		self.player = Player()
		self.all_sprites.add(self.player)
		b4 = Boundaries(0, HEIGHT*3/10, WIDTH * 3/4, 20)
		self.all_sprites.add(b4)
		self.boundaries.add(b4)
		b5 = Boundaries(WIDTH/4, 350, WIDTH * 3/4, 20)
		self.all_sprites.add(b5)
		self.boundaries.add(b5)
		b6 = Boundaries(0, HEIGHT*3/4, WIDTH * 3/4, 20)
		self.all_sprites.add(b6)
		self.boundaries.add(b6)
		self.PU1 = PowerUp(WIDTH/8, HEIGHT/8)
		self.all_sprites.add(self.PU1)
		self.power_up.add(self.PU1)
		self.PU2 = PowerUp(WIDTH/4, HEIGHT*7/8)
		self.all_sprites.add(self.PU2)
		self.power_up.add(self.PU2)
		self.PU3 = PowerUp(WIDTH/2, HEIGHT/8)
		self.all_sprites.add(self.PU3)
		self.power_up.add(self.PU3)
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
		hits = pg.sprite.spritecollide(self.player, self.boundaries, False)
		hits_item = pg.sprite.spritecollide(self.player, self.power_up, True)
		hits_platform = pg.sprite.spritecollide(self.player, self.platforms, False)
		if hits:
			self.player.pos.y = hits[0].rect.top
			self.player.vel.y = 0
			if hits[0].rect.top or hits[0].rect.left:
				self.jogando = False
		if self.player.pos.x + 30 > WIDTH or self.player.pos.x < 0:
			self.jogando = False
		if self.player.pos.y > HEIGHT or self.player.pos.y < 0:
			self.jogando = False

		if hits_item:
			if hits_item[0].rect:
				self.PU1.item +=1
				pg.mixer.Sound.play(pg.mixer.Sound("coin1.wav"))

			if self.PU1.item == 3:
				pouso = Platform(7*WIDTH/8, HEIGHT-150, 50,20)
				self.all_sprites.add(pouso)
				self.platforms.add(pouso)

		if hits_platform:
			if hits_platform[0].rect.top:
				if self.player.vel.y >= 3:
					self.jogando = False
				else:
					if self.player.pos.y - hits_platform[0].rect.top<=5:
						self.pouso = True
					else:
						self.jogando = False


	def events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				if self.jogando:
					self.jogando = False
				self.rodando = False


	def draw(self):
		self.screen.fill(spacial)
		self.all_sprites.draw(self.screen)
		self.draw_text(str(self.player.fuel), 22, branco, WIDTH/2 , 15)
		self.draw_text("[{0:.02f}, {1:.02f}]".format(self.player.vel[0], self.player.vel[1]),22, branco, 2/3* WIDTH, 15)
		pg.display.flip()

	def show_start_screen(self):
		self.screen.fill(pfcolor)
		self.draw_text(TITLE, 48, azulaleatorio, WIDTH/2, HEIGHT/4)
		self.draw_text("Use as setas para se movimentar!", 22, branco, WIDTH/2, HEIGHT/2)
		self.draw_text("Aperte qualquer botão para iniciar", 22, preto, WIDTH/2, HEIGHT*3/4)
		pg.display.flip()
		self.espera_por_tecla()


	def show_go_screen(self):
		if not self.rodando:
			return
		self.screen.fill(preto)
		self.draw_text("GAME OVER", 78, vermelho, WIDTH/2, HEIGHT/4)
		self.draw_text("Score:"+ str(self.player.fuel), 50, verde, WIDTH/2, HEIGHT/2)
		pg.display.flip()
		self.espera_por_tecla()

	def tela_vitoria(self):
		self.screen.fill(amarelo)
		self.draw_text("Parabéns!", 78, vermelho, WIDTH/2, HEIGHT/4)
		self.draw_text("Você conseguiu pousar a nave com sucesso!", 44, preto, WIDTH/2, HEIGHT/2)
		pg.display.flip()
		esperando = True
		while esperando:
			self.clock.tick(FPS)
			for event in pg.event.get():
				if event.type == pg.QUIT:
					esperando = False
					self.rodando = False
				if event.type == pg.KEYUP:
					esperando = False

	def espera_por_tecla(self):
		esperando = True
		while esperando:
			self.clock.tick(FPS)
			for event in pg.event.get():
				if event.type == pg.QUIT:
					esperando = False
					self.rodando = False
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
fase = 1
while g.rodando:
	if fase == 1:
	    g.new()
	elif fase == 2:
		g.new_2()
	if g.pouso == True:
		g.tela_vitoria()
		g.pouso = False
		fase +=1
	else:
		g.show_go_screen()

	if fase > 2:
		g.rodando = False

pg.quit()
