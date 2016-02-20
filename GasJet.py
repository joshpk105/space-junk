import pygame
import random

class GasJet():
  def __init__(self,jet_direction,transparent,color):
    self.jet_dir = jet_direction
    self.particles = []
    self.transparent = transparent
    self.color = color

  def fire(self,position):
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

  def draw(self,surface):
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




