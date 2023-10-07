# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alukongo <alukongo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/07/14 21:33:47 by alukongo          #+#    #+#              #
#    Updated: 2022/07/21 21:07:01 by alukongo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pygame
from player import player
from monster import Monster

class Game:
	def __init__(self):
		self.is_playing = False
		self.all_player = pygame.sprite.Group()
		self.player = player(self)
		self.all_player.add(self.player)
		self.all_monsters = pygame.sprite.Group()
		self.pressed = {}
		self.spawn_monster()
		self.spawn_monster()

	def start(self):
		self.is_playing = True
		self.spawn_monster()
		self.spawn_monster()

	def game_over(self):
		self.all_monsters = pygame.sprite.Group()
		self.player.health = self.player.health_max
		self.is_playing = False


	def update(self, screen):
		screen.blit(self.player.image, self.player.rect)

		self.player.update_health_bar(screen)

		self.player.update_animation()


		for projectile in self.player.all_projectiles:
			projectile.move()

		for monster in self.all_monsters:
				monster.forward()
				monster.update_health_bar(screen)
				monster.update_animation()

		self.player.all_projectiles.draw(screen)

		self.all_monsters.draw(screen)


		#here i manage the event
		if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 735:
			self.player.move_right()
		elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
			self.player.move_left()
		elif self.pressed.get(pygame.K_UP) and self.player.rect.y > 400:
			self.player.move_up()
		elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y < 555:
			self.player.move_down()

		#it for the display
		pygame.display.flip()

	def check_colision(self, sprite, group):
		return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

	def spawn_monster(self):
		monster = Monster(self)
		self.all_monsters.add(monster)
		monster.update_animation()