import pygame
import random
import math

class Particle():
  def __init__(self,position,angle,delta,life):
    self.pos = ([position[0],position[1]])
    self.real = (float(position[0]),float(position[1]))
    self.angle = float(angle)
    self.delta = float(delta)
    self.life = life

  def update(self):
    self.real = (self.real[0]+(self.delta*math.cos(self.angle)),
                 (self.real[1]+(self.delta*math.sin(self.angle))))
    self.pos = (int(self.real[0]),int(self.real[1]))
    self.life -= 1

  def quick_print(self):
    print ','.join(map(str,[self.pos,self.real,self.life]))