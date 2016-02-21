import pygame
import random
import Particle
import Cell

class GasJet():
  def __init__(self,jet_direction,transparent,color,cell):
    self.jet_dir = jet_direction
    self.particles = []
    self.transparent = transparent
    self.color = color
    self.cell = cell

  def rand_slope(self):
    m = 0
    if(self.jet_dir == 'n' or self.jet_dir == 's'):
      y = random.randint(2,9)
      x = random.randint(1,y-1)
      m = float(y)/float(x)
    else:
      x = random.randint(2,9)
      y = random.randint(1,x-1)
      m = float(y)/float(x)
    n = random.randint(1,2)
    #if(n == 1):
    #  m *= -1.0
    return(m)

  def fire(self):
    for i in range(random.randint(5,10)):
      p = Particle.Particle(self.cell.center,self.rand_slope(),1,10)
      self.particles.append(p)

  def draw(self,surface):
    updated = []
    for p in self.particles:
      print(str(p.pos))
      cur_color = surface.get_at(p.pos)
      if not (self.isTransparent(cur_color)):
        surface.set_at(p.pos,self.transparent)
      p.jet_update(self.jet_dir)
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

  def fire_old(self,position):
    for i in range(9):
      if(self.jet_dir == 'n' or self.jet_dir == 's'):
        num = random.randint(1,10)
        den = 0;
        if(num == 1):
          den = 1
        else:
          den = random.randint(1,num)
        m = float(num)/float(den)
        m = random.randint(-1,1)*float(m)
        self.particles.append((m,position,10))
      else:
        print("ew")

  def draw_old(self,surface):
    parts = []
    for m,pos,life in self.particles:
      new_pos = pos
      if(life == 0):
        continue
      if(self.jet_direction == 'n'):
        new_pos[0] = float(new_pos[0])-(1.0/m)
        new_pos[1] = float(new_pos[1])-m
      to_set = (int(new_pos[0]),int(new_pos[1]))
      old_pos = (int(pos[0]),int(pos[1]))
      surface.set_at(to_set,self.color)
      surface.set_at(old_pos.self.transparent)
      life = life-1
      parts.append((m,pos,life))
    self.particles = parts
    return surface




