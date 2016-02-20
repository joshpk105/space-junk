import pygame

class Resource():
    """description of class"""
    def __init__(self,rect,color):
      self.rect = rect
      self.color = color
      
    def overlap(self,test_rect):
      return pygame.Rect.colliderect(test_rect)

    


