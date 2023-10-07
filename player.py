from signal import pause
from time import sleep
from pip import main
import pygame
import animation


import animation
from monster import Monster

from projectile import projectile

class player(animation.animatesprite):
	def __init__(self, game):
		super().__init__("ninja")
		self.game = game
		self.health_max = 100
		self.health = 100
		self.attack = 10
		self.velocity = 1
		self.all_projectiles = pygame.sprite.Group()
		self.image = pygame.image.load("asset/ninja.png")
		#self.run = pygame.image.load("asset/ninja/ninja/ninja1.png")
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 430

	def update_animation(self):
		self.animate()
  		#if self.event.type == pygame.KEYUP:
		#	player.image = pygame.image.load("asset/ninja.png")
	#if self.anima == False:
		#	self.image = pygame.image.load("asset/ninja.png")
  

	def damage_hero(self, amount):
		if self.health - amount > 0:
			self.health -= amount
		else:
			self.game.game_over()

	def update_health_bar(self, surface):
		bar_position = [self.rect.x - 30, self.rect.y - 20, self.health, 5]
		dark_bar_position = [self.rect.x - 30, self.rect.y - 20, self.health_max, 5]
		pygame.draw.rect(surface, (169, 164, 162), dark_bar_position)
		pygame.draw.rect(surface, (111,210,46), bar_position)

	def launch_projectile(self):
		self.all_projectiles.add(projectile(self))

	def move_left(self):
		#self.image = pygame.image.load("asset/ninja/rivers_run/run_revers.png")
		self.start_animation()
		if not self.game.check_colision(self, self.game.all_monsters):
			self.rect.x -= self.velocity

	def move_right(self):
		self.start_animation()
		if not self.game.check_colision(self, self.game.all_monsters):
			self.rect.x += self.velocity

	def move_up(self):
		self.start_animation()
		self.rect.y -= self.velocity
		#self.image = pygame.image.load("asset/ninja/ninja/ninja1.png")

	def move_down(self):
		self.start_animation()
		#print(self.anima)
		self.rect.y += self.velocity

