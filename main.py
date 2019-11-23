import pygame

########################
print('MADE BY drogi17')
########################
print('To clear press (x)....')

speed = 0

win_x = 800
win_y = 800

pygame.init()
win = pygame.display.set_mode((win_x, win_y))   # отображение окна
pygame.display.set_caption("v1")                # заголовок окна

barriers = [[[100, 100], [100, 400]]]#, [[600, 100], [600, 400]]]
cent = [win_x/2, win_y/2]
cursor = pygame.mouse.get_pos
angle = 0
color_1 = 0
color_2 = 0
color_3 = 0
r = 1
win.fill((0, 0, 0))
run = True
while run:
    pygame.time.delay(int(speed))

    for event in pygame.event.get():    #quit
        if event.type == pygame.QUIT:   #quit
            run = False                 #quit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
            	win.fill((0, 0, 0))

    cursor = list(pygame.mouse.get_pos())
    pygame.draw.aaline(win, (color_1, color_2, color_3), cent, cursor)
    #print(str(color_1), str(color_2), str(color_3))
    if (color_1 < 225) and (r == 1):
    	color_1 += 1
    elif (color_1 == 225) and (color_2 < 225) and (r == 1):
    	color_2 += 1
    elif (color_2 == 225) and (color_3 < 225) and (r == 1):
    	color_3 += 1
    elif (color_3 == 225) and (r == 1):
    	color_1 = 0
    	color_2 = 0
    	color_3 = 0
    	r = 3
    elif (color_2 < 225) and (r == 2):
    	color_2 += 1
    elif (color_2 == 225) and (color_3 < 225) and (r == 2):
    	color_3 += 1
    elif (color_3 == 225) and (color_1 < 225) and (r == 2):
    	color_1 += 1
    elif (color_1 == 225) and (r == 2):
    	color_1 = 0
    	color_2 = 0
    	color_3 = 0
    	r = 4
    elif (color_3 < 225) and (r == 3):
    	color_3 += 1
    elif (color_3 == 225) and (color_2 < 225) and (r == 3):
    	color_2 += 1
    elif (color_2 == 225) and (color_1 < 225) and (r == 3):
    	color_1 += 1
    elif (color_1 == 225) and (r == 3):
    	color_1 = 0
    	color_2 = 0
    	color_3 = 0
    	r = 2
    elif (color_1 < 225) and (r == 4):
    	color_1 += 1
    elif (color_1 == 225) and (color_3 < 225) and (r == 4):
    	color_3 += 1
    elif (color_3 == 225) and (color_2 < 225) and (r == 4):
    	color_2 += 1
    elif (color_2 == 225) and (r == 4):
    	color_1 = 0
    	color_2 = 0
    	color_3 = 0
    	r = 1
    pygame.display.update()