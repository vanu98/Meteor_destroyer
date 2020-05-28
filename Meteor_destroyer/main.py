import pygame
import random
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode([screen_width, screen_height])
background = pygame.image.load('assets/bg.png').convert()
background_rect = background.get_rect()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
bloc_list = pygame.sprite.Group()

class Block(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		#self.image = pygame.Surface([width,height])
		self.image = pygame.image.load("assets/enemy.png").convert_alpha()
#		self.image.fill(color)
		self.rect = self.image.get_rect()
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		#self.image = pygame.Surface([width,height])
		#self.image.fill(color)
		self.image = pygame.image.load("assets/hull.png").convert_alpha()
		self.rect = self.image.get_rect()
class Bullet(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		#self.image = pygame.Surface([1,1])
#		self.image.fill(RED)
		self.image = pygame.image.load("assets/Bullet.png").convert_alpha()
		self.rect = self.image.get_rect()
	def update(self):
		self.rect.y -=3
def new_block():
	for i in range(50):
		block = Block()

		block.rect.x = random.randrange(10,screen_width)
		block.rect.y = random.randrange(10,600)
		bloc_list.add(block)
		block_list.add(block)
		all_sprites_list.add(block)
new_block()
player  = Player()
all_sprites_list.add(player)

player.rect.y = 370
done = False
clock = pygame.time.Clock()

score = 0

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			bullet = Bullet()
			bullet.rect.x = player.rect.x
			bullet.rect.y = player.rect.y
			
			all_sprites_list.add(bullet)
			bullet_list.add(bullet)
	all_sprites_list.update()
	
	for bullet in bullet_list:
		blocks_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
		
		for block in blocks_hit_list:
			bullet_list.remove(bullet)
			all_sprites_list.remove(bullet)
			score+=1
			print(score)
			
		if bullet.rect.y < 10:
			bullet_list.remove(bullet)
			all_sprites_list.remove(bullet)
	screen.blit(background, background_rect)
	if len(bloc_list)<25:
		new_block()
	pos = pygame.mouse.get_pos()

	player.rect.x = pos[0]
	player.rect.y = 800
	sc = str(score)
	scoree = myfont.render('Score='+sc,False,(0,0,0))
#	blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)


#	for block in blocks_hit_list:
#		score+=1
#		print(score)'''
	all_sprites_list.draw(screen)
	screen.blit(scoree,(0,0))
	clock.tick(60)
	pygame.display.flip()
pygame.quit()