# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alukongo <alukongo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/07/15 14:12:25 by alukongo          #+#    #+#              #
#    Updated: 2022/07/21 21:21:41 by alukongo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from asyncio import events
from curses import KEY_RIGHT
from email.mime import image
from time import sleep

import pygame
import math

from game import Game
from player import player

pygame.init()

pygame.display.set_caption("fenetre")

screen = pygame.display.set_mode((790, 690))

background = pygame.image.load("asset/background/foret.jpg")

banner = pygame.image.load("asset/background/Acceuil.png")

button_play = pygame.image.load("asset/background/button_play.png")

game = Game()

button_play_rect = button_play.get_rect()
button_play_rect.x = math.ceil(screen.get_width() / 2.5) 
button_play_rect.y = math.ceil(screen.get_height() / 1.5) 

running = True

while running:
	screen.blit(background,(0,0))
	if game.is_playing:
		game.update(screen)
	else:
		screen.blit(banner, (0,0))
		screen.blit(button_play, button_play_rect)

	pygame.display.flip()
		
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
		elif event.type == pygame.KEYDOWN:
			game.pressed[event.key] = True
			if event.key == pygame.K_SPACE:
				game.player.launch_projectile()
		elif event.type == pygame.KEYUP:
			game.pressed[event.key] = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if button_play_rect.collidepoint(event.pos):
				game.start()
				player.image = pygame.image.load("asset/ninja.png")
