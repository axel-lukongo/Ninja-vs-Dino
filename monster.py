import pygame
import random
import animation

class Monster(animation.animatesprite):
	def __init__(self, game):
		super().__init__("dino")
		self.game = game
		self.health = 100
		self.health_max = 100
		self.attack = 0.5
		#self.image = pygame.image.load("asset/dino/dino_walk/Walk1.png")
		self.rect = self.image.get_rect()
		self.rect.x = 500 + random.randint(0, 300)
		self.rect.y = 420
		self.velocity = random.randint(1, 1)
	
	def damage(self, amount):
		self.health -= amount
		if self.health <= 0:
			self.rect.x = 650
			self.rect.y = random.randint(400, 555)
			self.velocity = random.randint(1, 1)
			self.health = self.health_max

	def update_animation(self):
		self.start_animation()
		self.animate()

	def update_health_bar(self, surface):
		bar_position = [self.rect.x + 40, self.rect.y - 10, self.health, 5]
		dark_bar_position = [self.rect.x + 40, self.rect.y - 10, self.health_max, 5]
		pygame.draw.rect(surface, (169, 164, 162), dark_bar_position)
		pygame.draw.rect(surface, (111,210,46), bar_position)

	def forward(self):
		if not self.game.check_colision(self, self.game.all_player):
			self.rect.x -= self.velocity
		else:
			self.game.player.damage_hero(self.attack)

	def backward(self):
		self.image = pygame.image.load("asset/dino/dino_walk_revers/Walk1.png")
		if self.rect.x < 500:
			self.rect.x += self.velocity