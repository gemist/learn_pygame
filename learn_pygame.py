import pygame
import random

def CheckCollision(playerX,playerY,testX,testY, testWidth, testHeight):
    global playerHeight, playerWidth,enemyX, enemyY, enemyXstart,enemyYstart
    collisionState = False
    if playerHeight <= testHeight:
        if playerY + playerHeight >= testY  and playerY + playerHeight <= testY + testHeight:
            if playerX + playerWidth >= testX  and playerX + playerWidth <= testX + testWidth:
                playerY = playerYstart
                playerX = playerXstart
                enemyX = enemyXstart
                enemyY = enemyYstart
                collisionState = True
            elif playerX >= testX and playerX <= testX + testWidth:
                playerY = playerYstart
                playerX = playerXstart
                enemyX = enemyXstart
                enemyY = enemyYstart
                collisionState = True
        elif playerY >= testY  and playerY <= testY + testHeight:
            if playerX + playerWidth >= testX  and playerX + playerWidth <= testX + testWidth:
                playerY = playerYstart
                playerX = playerXstart
                enemyX = enemyXstart
                enemyY = enemyYstart
                collisionState = True
            elif playerX >= testX and playerX <= testX + testWidth:
                playerY = playerYstart
                playerX = playerXstart
                enemyX = enemyXstart
                enemyY = enemyYstart
                collisionState = True
    else:
        if testY + testHeight >= playerY  and testY + testHeight <= playerY + playerHeight:
            if testX + testWidth >= playerX  and testX + testWidth <= playerX + playerWidth:
                playerY = playerYstart
                playerX = playerXstart
                enemyX = enemyXstart
                enemyY = enemyYstart
                collisionState = True
            elif testX >= playerX and testX <= playerX + playerWidth:
                playerY = playerYstart
                playerX = playerXstart
                enemyX = enemyXstart
                enemyY = enemyYstart
                collisionState = True
        elif testY >= playerY  and testY <= playerY + playerHeight:
            if testX + testWidth >= playerX  and testX + testWidth <= playerX + playerWidth:
                playerY = playerYstart
                playerX = playerXstart
                enemyX = enemyXstart
                enemyY = enemyYstart
                collisionState = True
            elif testX >= playerX and testX <= playerX + playerWidth:
                playerY = playerYstart
                playerX = playerXstart
                enemyX = enemyXstart
                enemyY = enemyYstart
                collisionState = True

    return collisionState, playerY, playerX


screenWidth = 700
screenHeight = 700 

treasureHeight = treasureWidth = 50
playerHeight = playerWidth = enemyHeight = enemyWidth = 80
playerXstart = playerX = screenWidth/2-playerWidth/2
playerYstart = playerY = 620
playerStep = 5

treasureX = screenWidth/2 - treasureWidth/2 
treasureY = 50

enemyXstart = enemyX = 50
enemyYstart = enemyY = 50
enemyStep = 4

pygame.init()
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Dejko the Great - Mineral Hunter")

finished = False 

playerImage = pygame.image.load("img/player.png")
playerImage = pygame.transform.scale(playerImage,(playerWidth,playerHeight))
playerImage = playerImage.convert_alpha()

enemyImage = pygame.image.load("img/enemy.png")
enemyImage = pygame.transform.scale(enemyImage,(enemyWidth,enemyHeight))
enemyImage = enemyImage.convert_alpha()


backgroundImage = pygame.image.load("img/ground.png")
backgroundImage = pygame.transform.scale(backgroundImage,(screenWidth,screenHeight))

treasureImage = pygame.image.load("img/mineral.png")
treasureImage = pygame.transform.scale(treasureImage,(treasureWidth,treasureHeight))
treasureImage = treasureImage.convert_alpha()

screen.blit(backgroundImage,(0,0))
screen.blit(treasureImage,(treasureX,treasureY))

font = pygame.font.SysFont("comicsans",60)

level = 1

frame = pygame.time.Clock()
collisionTreasure = False
collisionEnemy = False


while finished == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            finished = True

			
    pressedKeys = pygame.key.get_pressed()	# [...,UP,DOWN,LEFT,RIGHT,...]

    
    distanceX = playerX - enemyX
    distanceY = playerY - enemyY
    distanceSq = distanceX*distanceX + distanceY*distanceY
    
    #if movingEnemy == True:
    enemyXtmp = enemyX + enemyStep*random.randrange(-1,2)*level
    enemyYtmp = enemyY + enemyStep*random.randrange(-1,2)*level

    distanceX = playerX - enemyXtmp 
    distanceY = playerY - enemyYtmp 
    distanceSqTmp = distanceX*distanceX + distanceY*distanceY
    if distanceSqTmp  <= distanceSq:
        enemyX = enemyXtmp
        enemyY = enemyYtmp
            

    if pressedKeys[pygame.K_UP] == 1:
        playerY -= playerStep
    if pressedKeys[pygame.K_DOWN] == 1:
        playerY += playerStep
    if pressedKeys[pygame.K_RIGHT] == 1:
        playerX += playerStep
    if pressedKeys[pygame.K_LEFT] == 1:
        playerX -= playerStep


    if playerX > screenWidth - playerWidth:
        playerX = screenWidth - playerWidth
    elif playerX < 0:
        playerX = 0

    if playerY > screenHeight - playerHeight:
       playerY = screenHeight - playerHeight
    elif playerY < 0:
       playerY = 0

        
    screen.blit(backgroundImage,(0,0))
    screen.blit(treasureImage,(treasureX,treasureY))
    screen.blit(playerImage,(playerX,playerY))
    screen.blit(enemyImage,(enemyX,enemyY))
    
    collisionTreasure, playerY, playerX  = CheckCollision(playerX,playerY,treasureX,treasureY,treasureWidth,treasureHeight)
    if collisionTreasure == True:
        level += 1
        textWin = font.render("You have reached level " + str(level),True,(0,0,0))
        screen.blit(textWin,(screenWidth/2 - textWin.get_width()/2,screenHeight/2 - textWin.get_height()/2))
        pygame.display.flip() #update screen
        frame.tick(1)

    collisionEnemy, playerY, playerX  = CheckCollision(playerX,playerY,enemyX,enemyY,enemyWidth,enemyHeight)
    if collisionEnemy == True:
        textLose = font.render("Caught by Honolulu police!",True,(255,0,0))
        screen.blit(textLose,(screenWidth/2 - textLose.get_width()/2,screenHeight/2 - textLose.get_height()/2))
        pygame.display.flip() #update screen
        frame.tick(1)
        
    pygame.display.flip() #update screen
    frame.tick(30)
