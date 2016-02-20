import pygame
import Resource
import numpy.random
import random
import Genome

class ResourceMap():
    """description of class"""
    def __init__(self,surface,total,resource):
      self.surface = surface
      self.total = total
      self.resource = resource
      self.resources = []
      self.Generate()

    def Generate(self):
      for i in range(self.total):
        (red_delta,green_delta,blue_delta) = map(int,numpy.random.normal(125,40,3))
        red_delta = self.Correct(red_delta)
        green_delta = self.Correct(green_delta)
        blue_delta = self.Correct(blue_delta)
        (width,height) = self.surface.get_size()
        rand_x = random.randrange(width-self.resource.rect.width)
        rand_y = random.randrange(height-self.resource.rect.height)
        self.resources.append(Resource.Resource(pygame.Rect(rand_x,rand_y,
                   self.resource.rect.width,self.resource.rect.height)
                   ,(red_delta,blue_delta,green_delta)))

    def Correct(self,value):
      if(value < 0):
        return 0
      if(value > 250):
        return 250
      return value

    def Draw(self):
      for r in self.resources:
        pygame.draw.rect(self.surface,r.color,r.rect,0)

    def Collision(self,genome):
      for r in self.resources:
        if(genome.collide(r.rect)):
          self.resources.remove(r)
          print "Hit"
          self.surface.fill((125,125,125))
          self.Draw()



