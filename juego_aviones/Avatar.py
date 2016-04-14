import pygame
from Assets import assets
from GameState import *
#from Analizer import *
#import gevent

debug = False;

class Avatar(pygame.sprite.DirtySprite):
	def __init__(self,width, height):
		pygame.sprite.Sprite.__init__(self)
		self.width = width
		self.height = height
		self.image = assets["avatar"]
		self.image = pygame.transform.scale(self.image,(50,50))
		self.rect = self.image.get_rect()
		self.rect.y = self.height - self.rect.h - 100
		self.rect.x = (self.width - self.rect.w)/2
		self.blink = False
		self.blinkCount = 0
		self.blinkState = 0
		self.allSprites = None
		self.enemies = None
		self.leftFrec = 8 
		self.rightFrec = 12
		self.useAnalizer = True
		self.horizontalSpeed = 3
		pass
	def startBlink(self):
		if self.blink == False:
			self.blinkCount =0
			self.blink =True
		pass
	def calculateBlink(self):
		if self.blink :
				self.blinkCount += 1
				if self.blinkCount % 10 == 0:
					self.blinkState = 1 if self.blinkState ==2 else 2
					if self.blinkState == 1:
						self.allSprites.add(self)
					else:
						self.allSprites.remove(self)
				if self.blinkCount > 300:
					self.blink = False
					self.blinkState = 1
					self.allSprites.add(self)
		pass
	def moveRight(self):
		speed=[self.horizontalSpeed,0]
		self.move(speed)
		pass
	def moveLeft(self):
		speed=[-self.horizontalSpeed,0]
		self.move(speed)
		pass
	def move(self,speed):
		self.rect = self.rect.move(speed)
		if(self.rect.x < 0):
			self.rect.x = 0
		if(self.rect.x > self.width-self.rect.w ):
			self.rect.x = self.width-self.rect.w
			
		pass
	def update(self,*args):
		gameState = args[0]
		if gameState.state == PLAYING:
			
			mouse =  pygame.mouse.get_pressed()
			keys = pygame.key.get_pressed()

			if debug:
				print "Pressed buttons :",mouse		
			if (mouse[0] == 1 and mouse[2] == 1) == False:
				if mouse[0]  or keys[pygame.K_LEFT]: #left click
					self.moveLeft()
				elif mouse[2]  or keys[pygame.K_RIGHT]:  #right click
					self.moveRight()
			self.calculateBlink()
		elif gameState.state == ENDED:
			mouse =  pygame.mouse.get_pressed()
			if mouse[0] :
				gameState.reset()
				gameState.resume()
		pass
