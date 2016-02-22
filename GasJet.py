import pygame
import random
import Particle
import Cell
import math

class GasJet():
  def __init__(self,jet_direction,transparent,color,cell):
    self.jet_dir = jet_direction
    self.particles = []
    self.transparent = transparent
    self.color = color
    self.cell = cell

  def rand_radians(self):
    radians = 0
    if(self.jet_dir == 'n'):
      radians = random.uniform(math.pi/4,(3.0/4.0)*math.pi)
    elif(self.jet_dir == 's'):
      radians = random.uniform((5.0/4.0)*math.pi,(7.0/4.0)*math.pi)
    elif(self.jet_dir == 'e'):
      if(random.randint(1,2) == 1):
        radians = random.uniform((0),(math.pi/4))
      else:
        radians = random.uniform((7.0/4.0)*math.pi,(2*math.pi))
    elif(self.jet_dir == 'w'):
      radians = random.uniform(((3.0/4.0)*math.pi),(5.0/4.0)*math.pi)
    else:
      print('Jet direction doesn not exist')
    return(radians)

  def fire(self):
    for i in range(random.randint(5,10)):
      p = Particle.Particle(self.cell.center,self.rand_radians(),random.randint(2,5),random.randint(10,20))
      self.particles.append(p)

  def draw(self,surface):
    updated = []
    for p in self.particles:
      #print(str(p.pos))
      cur_color = surface.get_at(p.pos)
      if not (self.isTransparent(cur_color)):
        surface.set_at(p.pos,self.transparent)
      p.update()
      if(p.life > 0):
        surface.set_at(p.pos,self.color)
        updated.append(p)

    self.particles = updated
    return(surface)
      

  def isTransparent(self,color):
    if(color[0] == self.transparent[0] and color[1] == self.transparent[1] and
       color[2] == self.transparent[2]):
      return True;
    return False;




