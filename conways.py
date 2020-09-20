'''
-conway's game of life
-made by Tzara Northcut @Mecknavorz
-requires pygame
'''

#import the stuff we need
import pygame, sys, time

#-----------------------------------------
#initalize some variables and other things
#-----------------------------------------
width = 6 #cell size width
height = 6 #cell size height
space = 2 #thickness of world lines
#create the 2d array where we actually store vairables of cells
world = [[0 for x in range(100)] for y in range(100)]

#initialzie pygame
pygame.init()

size = [100*(width+space)+space, 100*(height+space)+space] #window size
screen = pygame.display.set_mode(size) #make the window the right size

#set spme colors
BLACK = (  0,   0,   0) #background color
WHITE = (255, 255, 255) #color of world
GREEN = (  0,   0,   0) #color of cells that are alive and well
RED = (255,   0,   0) #colors of the cells about to die

#speed stuff
clock = pygame.time.Clock() #clock used to manage game speed
pause = True #used to control the steps, might not need this
laststep = time.time()

#used to keep runing until the game is closed
done = False

#-------------------------------------
#some functions to be used in the game
#-------------------------------------
#determine #of cells nearby
def getclose(x, y):
    nearby = 0
    #avoid out of bounds error and make the grid a torroid
    if(x+1) > 99:
        x = 0
    if(y+1) > 99:
        y = 0
    #swcan nearby squares and if there's something there add 1 to the count
    if world[x-1][y-1]:
        nearby += 1
    if world[x][y-1]:
        nearby += 1
    if world[x+1][y-1]:
        nearby += 1
    if world[x-1][y]:
        nearby += 1
    if world[x+1][y]:
        nearby += 1
    if world[x-1][y+1]:
        nearby += 1
    if world[x][y+1]:
        nearby += 1
    if world[x+1][y+1]:
        nearby += 1
    return nearby

#calculate next step
def nextStep():
    for x in range(len(world)):
        for y in range(len(world[0])):
            near = getclose(x, y)
            if near < 2: #if there are less than two neighbors then kill the cell
                world[x][y] = 0
            if near > 3: #if there are more than three neighbors then kill the cell
                world[x][y] = 0
            if (world[x][y] == 0) and (near == 3): #if there are 3 neighbors near a dead cell, revive it
                world[x][y] = 1

#clear the board
def clear():
    for x in range(len(world)):
        for y in range(len(world[0])):
            world[x][y] = 0

#---------------------
#the initale game loop
#---------------------
while not done:
    #to make sure the game quits when we need it to
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN: #if we get a click
            pos = pygame.mouse.get_pos() #find where the click was
            #change the pixel coords into game coords
            x = pos[1] // (height+space)
            y = pos[0] // (width+space)
            #add or remove the cell that's there
            if world[x][y] == 0: #if the tile is empty add a cell
                world[x][y] = 1
                #print("nearby: ", getclose(x, y)) #used for debugging
            else: #else if there's something there, remove the cell
                world[x][y] = 0
            #print("click: ", pos, "grid coord: ", x, y) #debug stuff
        elif event.type == pygame.KEYDOWN: #pause the game when space is pressed
            if event.key == pygame.K_SPACE:
                #print('space pressed')
                if pause:
                    pause = False
                elif not pause:
                    pause = True
            elif event.key == pygame.K_RIGHT: #if we presws the right key go forward a step
                nextStep() #calculate the next
            elif event.key == pygame.K_ESCAPE:
                clear()
            

    #draw the world
    screen.fill(BLACK)
    #maybe move this to a seprate function to help with effeciency?
    for x in range(len(world)):
        for y in range(len(world[0])):
            color = WHITE
            if world[x][y] == 1:
                color = GREEN
            pygame.draw.rect(screen, color, [(space+width)*y+space, (space+height)*x+space, width, height])

    #set frame rate
    clock.tick(60)
    if (not pause) and ((time.time() - laststep) > .1):
        laststep = time.time()
        #print(laststep)
        nextStep()
    #update screen
    pygame.display.flip()

#if we;ve gotten this far (eg out of the while loop) we know it's time to quit
pygame.quit()
