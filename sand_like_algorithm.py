import pygame
import sys
import random
import math



pygame.init()
info = pygame.display.Info()
w, h = info.current_w, info.current_h
screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.RESIZABLE)
pygame.display.set_caption('physics, math, code & fun')

pygame.mixer.init()
beep = pygame.mixer.Sound("beep.mp3")
font = pygame.font.SysFont('Arial', 50)
clock = pygame.time.Clock()

size = 30
t = 0
delta_time = 0.0


class Particles:
    def __init__(self, x, y):
        self.rect =  pygame.Rect(x, y, size, size)
        self.visible = True
        self.enable = False
        self.color = [255,30,30]
        self.velocity = [0,0]
        self.dt = 0
        self.side_walk = 0
        self.max_side_walk = random.randint(0,15)
        self.dir = random.randint(0,1)
    def draw(self, screen):
        if self.visible:
            pygame.draw.rect(screen, self.color, self.rect)

            

particles = []
pixels = []

for i in range(0, w, size):
    aux = []
    for j in range(0, h, size):
        aux.append(0)
    pixels.append(aux)
  
for i in range(0, len(pixels)): 
    pixels[i][((h - 2*size) // size)] = 1

def Update(screen):
    global t
    global delta_time

    screen.fill((0,0,0))
    
    if t % 10 == 0 and len(particles) <= 300:
        particles.append(Particles(size * ((w // size)//2), 0))
        
        
        
    for l in range(0, len(particles)):     
        
        i = particles[l].rect.x // size
        j = particles[l].rect.y // size
                
        
        if pixels[i][j + 1] == 0:
            if particles[l].dt >= 50:
                particles[l].dt = 0
                particles[l].rect.y += size 
                pixels[i][j] = 0                
            else:
                particles[l].dt += size
        else:
            pixels[i][j] = 1
            if particles[l].side_walk <= particles[l].max_side_walk:       
                if pixels[i][j + 2] == 1:
                    if particles[l].dir == 0 and pixels[i + 1][j] == 0:
                        particles[l].rect.x += size 
                        pixels[i + 1][j] = 1
                        pixels[i][j] = 0  
                        particles[l].side_walk += 1  
                        beep.play()                        
                    elif particles[l].dir == 1 and pixels[i - 1][j] == 0:     
                        particles[l].rect.x -= size            
                        pixels[i - 1][j] = 1
                        pixels[i][j] = 0
                        particles[l].side_walk += 1
                        beep.play()          
            
        
        particles[l].draw(screen) 
    
    text = font.render('https://github.com/PhysicsMathCodeAndFun', True, (255,255,255))
    screen.blit(text, pygame.Rect(10, 0, 400,300))

    t += 1
    
    delta_time = clock.tick(60) / 1000
    pygame.display.flip()
    


isEnd = False
while not isEnd:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isEnd = True
            
    Update(screen)
    
pygame.quit()
sys.exit()
