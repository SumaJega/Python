import pygame
import sys
pygame.init()
size=width,height=1000,500
speed=[1,1]
background=255,255,255
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing Ball")
clock=pygame.time.Clock()
ball=pygame.image.load("ball.jpg")
ballrect=ball.get_rect()
clock=pygame.time.Clock()
while (True):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
	ballrect=ballrect.move(speed)
	if ballrect.left<0 or ballrect.right>width:
		speed[0]=-speed[0]
	if ballrect.top<0 or ballrect.bottom>height:
		speed[1]=-speed[1]
	screen.fill(background)
	screen.blit(ball,ballrect)	
	pygame.display.flip()
	clock.tick(300)
