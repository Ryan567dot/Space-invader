import pygame

pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Space Invader")

fire_rad = 10
fire_x = 250
fire_y = 10
fire_color = (255,255,0)

#BG color
bg_color = (0,0,0)

#Rocket
rc_color = (0,255,255)

rc_h = 30
rc_w = 15
rc_x = 250
rc_y = 400

while True:
    for event in pygame.event.get():
        if event. type == pygame.QUIT:
            pygame.QUIT()
    #Space
    window.fill(bg_color)
    
    if fire_y > 500:
        fire_y = 20
        fire_x = random.randint()
    else:
        fire_y = fire_y + 5
        
    key = pygame.key.get_pressed()
    if(key[pygame.K_LEFT]):
        rc_x = rc_x -5
    if(key[pygame.K_RIGHT]):
        rc_x = rc_x + 5
    if(key[pygame.K_UP]):
        rc_y = rc_y 
        
    #Fire
    pygame.draw.circle(window,fire_color,(fire_x,fire_y),fire_rad)
    #Rocket
    pygame.draw.rect(window,rc_color,(rc_x,rc_y,rc_w,rc_h))
    
    pygame.time.delay(100)
    
    pygame.display.flip()
    
pygame.quit()