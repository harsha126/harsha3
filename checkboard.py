import pygame
import time
import random
WIDTH,HEIGHT=588,588
FPS=75
BOX_HEIGHT=20
BOX_WIDTH=20
BOX_GAP=2
RED = (255,0,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
pygame.init()
surface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("checkboard")
all_xy=[x for x in range(0,HEIGHT,BOX_HEIGHT+BOX_GAP)]
x_choices=random.choices(all_xy,k=40)
y_choices=random.choices(all_xy,k=40)
check_board=[[0 for i in range(0,HEIGHT,(BOX_HEIGHT+BOX_GAP))] for j in range(0,WIDTH,(BOX_WIDTH+BOX_GAP))]

def draw_check_board():
	surface.fill(RED)
	for i in range(0,HEIGHT,BOX_HEIGHT+BOX_GAP):
		
		for j in range(0,WIDTH,BOX_WIDTH+BOX_GAP):

			pygame.draw.rect(surface,WHITE,pygame.Rect(i,j,BOX_HEIGHT,BOX_WIDTH),1)
			pygame.display.update()
	# for k in range(0,len(x_choices))	:
	# 	draw_rect_fill(x_choices[k],y_choices[k])
	pygame.display.update()

def paint_window(i,j):
	if check_board[i][j]==0:
		draw_rect_fill(i*(BOX_HEIGHT+BOX_GAP),j*(BOX_WIDTH+BOX_GAP))
		check_board[i][j]=1	
		
	else:
		draw_rect(i*(BOX_HEIGHT+BOX_GAP),j*(BOX_WIDTH+BOX_GAP))
		check_board[i][j]=0
		



def draw_rect_fill(i,j):
	pygame.draw.rect(surface,WHITE,pygame.Rect(i,j,BOX_HEIGHT,BOX_WIDTH))
	pygame.display.update()

def draw_rect(i,j):
	pygame.draw.rect(surface,RED,pygame.Rect(i,j,BOX_HEIGHT,BOX_WIDTH))
	pygame.draw.rect(surface,WHITE,pygame.Rect(i,j,BOX_HEIGHT,BOX_WIDTH),1)
	pygame.display.update()


draw_check_board()
run=True
while run:
	clock=pygame.time.Clock()
	for event in pygame.event.get():
		clock.tick(FPS)
		if event.type==pygame.QUIT:
			run=False
		elif event.type==pygame.MOUSEMOTION:
			if event.buttons==(1,0,0):
				print((event.pos[0]//(BOX_HEIGHT+BOX_GAP)),(event.pos[1]//(BOX_WIDTH+BOX_GAP)))
				# paint_window((event.pos[0]//(BOX_HEIGHT+BOX_GAP)),(event.pos[1]//(BOX_WIDTH+BOX_GAP)))
				draw_rect_fill((event.pos[0]//(BOX_HEIGHT+BOX_GAP))*(BOX_HEIGHT+BOX_GAP),(event.pos[1]//(BOX_WIDTH+BOX_GAP))*(BOX_HEIGHT+BOX_GAP))
			elif event.buttons==(0,0,1):
				draw_rect((event.pos[0]//(BOX_HEIGHT+BOX_GAP))*(BOX_HEIGHT+BOX_GAP),(event.pos[1]//(BOX_WIDTH+BOX_GAP))*(BOX_HEIGHT+BOX_GAP))
		elif event.type==pygame.MOUSEBUTTONDOWN:
			paint_window((event.pos[0]//(BOX_HEIGHT+BOX_GAP)),(event.pos[1]//(BOX_WIDTH+BOX_GAP)))
pygame.quit()



