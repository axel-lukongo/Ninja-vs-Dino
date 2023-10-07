import pygame
import player


class animatesprite(pygame.sprite.Sprite):
	def __init__(self, sprite_name):
		super().__init__()
		self.image = pygame.image.load("asset/" + sprite_name + ".png")
		self.current_image = 0
		self.images = animations.get(sprite_name)
		self.anima = False

	def start_animation(self):
		self.anima = True

	def animate(self):
		if self.anima:
			self.current_image += 1
			if self.current_image > 7:
				self.current_image = 0
				self.anima = False
			self.image = self.images[self.current_image]
			#if self.anima == False:
			#	self.image = pygame.image.load("asset/ninja.png")


def load_animation_images(sprite_name):
	
	images = []
	
	path = f"asset/{sprite_name}/{sprite_name}/{sprite_name}"

	for num in range(1, 10):
		image_path = path + str(num) + ".png"
		images.append(pygame.image.load(image_path))
	return images

animations = {
	"dino" : load_animation_images("dino"),
	"ninja" : load_animation_images("ninja")
}
