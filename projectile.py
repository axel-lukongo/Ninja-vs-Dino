from os import remove
from select import select
import pygame

class projectile(pygame.sprite.Sprite):
	def __init__(self, player):
		super().__init__()
		self.velocity = 3
		self.player = player
		self.image = pygame.image.load("asset/ninja/armed/Kunai.png")
		self.image = pygame.transform.scale(self.image, (40,10))
		self.rect = self.image.get_rect() 
		self.rect.x = player.rect.x + 20
		self.rect.y = player.rect.y + 40

	def remove(self):
		self.player.all_projectiles.remove(self)


	def move(self):
		self.rect.x += self.velocity 
		for monster in self.player.game.check_colision(self, self.player.game.all_monsters):
			self.remove()
			monster.damage(self.player.attack)
		if self.rect.x > 735:
			self.remove()