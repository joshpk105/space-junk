import pygame
import random

class Particle():
  def __init__(self,position,slope,delta,life):
    self.pos = position
    self.real = (float(position[0]),float(position[1]))
    self.m = slope
    self.d = delta
    self.life = life

  def update(self):
    delta_x = float(self.m)*float(self.delta)
    delta_y = 1.0/float(self.m) * float(self.delta)
    self.real = (self.real[0]+delta_x,self.real[1]+delta_y)
    self.pos = (int(self.real[0]),int(self.real[1]))
    self.life -= 1
