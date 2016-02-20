import pygame
import random

class SpaceBackground():
  def __init__(self,surface):
    (width,height) = surface.get_size()
    surface.fill((0,0,0))
    self.surface = surface
    for i in range(200):
      s_x = random.randint(0,width)
      s_y = random.randint(0,height)
      s_z = random.randint(1,3)
      self.star(s_z,s_x,s_y)
    self.surface = self.surface.convert()
  
  def star(self,z,x,y):
    pygame.draw.line(self.surface,(250,250,250),(x+z,y),(x-z,y),1)
    pygame.draw.line(self.surface,(250,250,250),(x,y+z),(x,y-z),1)
    for i in range(z):
      n = int((float(((z-i)**2))/float(z**2))*z)
      pygame.draw.line(self.surface,(250,250,250),((x+n),y-i),((x-n),y-i),1)
      pygame.draw.line(self.surface,(250,250,250),((x+n),y+i),((x-n),y+i),1)



