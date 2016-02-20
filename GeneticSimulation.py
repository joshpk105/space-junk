import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
#Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Garden')
    pygame.mouse.set_visible(0)

#Create The Backgound
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

#Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

#Prepare Game Objects
    clock = pygame.time.Clock()
    #whiff_sound = load_sound('whiff.wav')
    #punch_sound = load_sound('punch.wav')
    #chimp = Chimp()
    #fist = Fist()
    #allsprites = pygame.sprite.RenderPlain((fist, chimp))

#Main Loop
    while 1:
        clock.tick(60)

    #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            #elif event.type == MOUSEBUTTONDOWN:
                #if fist.punch(chimp):
                #    punch_sound.play() #punch
                #    chimp.punched()
                #else:
                #    whiff_sound.play() #miss
            #elif event.type is MOUSEBUTTONUP:
            #    fist.unpunch()

        #allsprites.update()

    #Draw Everything
        triangle = ((250,250),(200,200),(150,150))
        pygame.draw.polygon(background,0xFFFF66,triangle,0)
        screen.blit(background, (0, 0))
        #allsprites.draw(screen)
        pygame.display.flip()

#Game Over


#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()