import os, pygame, sys
from pygame.locals import *
import pygame.gfxdraw
import Cell
import Genome
import Resource
import ResourceMap
import SpaceBackground

def main():
  pygame.init()
  screen = pygame.display.set_mode((1000,1000))
  pygame.display.set_caption('Garden')
  background = SpaceBackground.SpaceBackground(pygame.Surface(screen.get_size()))
  
  foreground = pygame.Surface(screen.get_size())
  foreground.fill((125,125,125))
  foreground.set_colorkey((125,125,125))
  r = Resource.Resource(pygame.Rect(500,500,10,10),(250,0,0))
  res_map = ResourceMap.ResourceMap(foreground,10,r)
  genome_surface = pygame.Surface((500,500))
  #seed = Cell.Cell([(250,250),(200,250),(250,200)],(250,250,250))
  g = Genome.Genome(genome_surface,10,10,(125,125,126))
  #pygame.draw.circle(foreground,(250,250,250),(25,25),25,0)
  #pygame.image.save(foreground,'ball.bmp')
  speed = [0,0]
  #pygame.draw.circle(foreground,r.color,r.location,r.radius,0)
  pygame.draw.rect(foreground,r.color,r.rect,0)
  #triangle = Cell.Cell([[100,100],[100,300],[300,100]],(250,250,250))
  #pygame.gfxdraw.filled_polygon(background,triangle.points,triangle.color)

  #ball = pygame.image.load("ball.bmp")
  #ballrect = ball.get_rect()

  #background = background.convert()
  foreground = foreground.convert()
  pygame.display.flip()
  res_map.Draw()
  while 1:
    for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          g.AddCell()
          #genome_image = pygame.image.load(g.filename)
        if event.key == pygame.K_UP:
          speed[1] += -1
          g.north_jet.fire()
        if event.key == pygame.K_DOWN:
          speed[1] += 1
          g.south_jet.fire()
        if event.key == pygame.K_RIGHT:
          speed[0] += 1
          g.west_jet.fire()
        if event.key == pygame.K_LEFT:
          speed[0] += -1
          g.east_jet.fire()
        if event.key == pygame.K_q:
          g.rotate_center(-10)
          #genome_image = pygame.transform.rotate(genome_image,-10)
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
          speed[1] += 1
          g.south_jet.fire()
        if event.key == pygame.K_DOWN:
          speed[1] += -1
          g.north_jet.fire()
        if event.key == pygame.K_RIGHT:
          speed[0] += -1
          g.east_jet.fire()
        if event.key == pygame.K_LEFT:
          g.west_jet.fire()
          speed[0] += 1
    g.DrawParticles()
    g.move(speed)
    if(res_map.Collision(g)):
      print "Collision"

    screen.blit(background.surface,(0,0))
    screen.blit(g.particle_surface,g.loaded_rect)
    screen.blit(g.loaded,g.loaded_rect)
    screen.blit(res_map.surface,(0,0))
    
    pygame.display.flip()
    

if __name__ == '__main__': main()
