import pygame as pg
from config import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30,40))
        self.image.fill(azul)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/8, HEIGHT/4)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.fuel = 1000


    def update(self):
        self.acc = vec(0, 0.05)
        keys = pg.key.get_pressed()
        if self.fuel > 0:
            if keys[pg.K_LEFT]:
                self.acc.x = -PLAYER_ACC
                self.fuel -= 1
            if keys[pg.K_RIGHT]:
                self.acc.x = PLAYER_ACC
                self.fuel -= 1
            if keys[pg.K_UP]:
                self.acc.y = -PLAYER_ACC_UP
                self.fuel -= 1
            #aplica fricção
        self.acc.x += self.vel.x *PLAYER_FRICTION


        #movimentação
        self.vel += self.acc
        self.pos += self.vel + 0.3*self.acc
        #parte que impede que a nave fuja da tela

        self.rect.midbottom = self.pos

class Boundaries(pg.sprite.Sprite):
    def __init__(self,x,y,w,h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(verde)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Platform(pg.sprite.Sprite):
    def __init__(self,x,y,w,h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(vermelho)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class PowerUp(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((20, 20))
        self.image.fill(branco)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.item = 0
