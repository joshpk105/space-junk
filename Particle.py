import pygame
import random
import numpy as np

class Particle():
  def __init__(self,position,angle,delta,life):
    self.pos = np.array([position[0],position[1]])
    self.real = np.array([float(position[0]),float(position[1])])
    self.angle = float(angle)
    self.delta = np.array([float(angle),float(delta)])
    self.life = life

  def vector_update(self):
    print(self.real)
    self.real = self.real.dot(self.delta)
    print(self.real)

  def update(self):
    delta_x = 1.0/float(self.m)*float(self.d)
    delta_y = float(self.m) * float(self.d)
    self.real = (self.real[0]+delta_x,self.real[1]+delta_y)
    self.pos = (int(self.real[0]),int(self.real[1]))
    self.life -= 1
  
  def jet_update(self,direct):
    delta_x = 1.0/float(self.m)*float(self.d)
    delta_y = float(self.m) * float(self.d)
    if(direct == 'n' and self.m < 0):
      delta_x *= -1.0
    if(direct == 's'):
      delta_x *= -1.0
      delta_y *= -1.0
    self.real = (self.real[0]+delta_x,self.real[1]+delta_y)
    self.pos = (int(self.real[0]),int(self.real[1]))
    self.life -= 1

  def quick_print(self):
    print ','.join(map(str,[self.pos,self.real,self.life]))