import pygame
import math

class Cell:
    """description of class"""
    def __init__(self,points,color,cell_w,cell_h):
      self.index = points
      self.color = color
      if((points[0] % 2 == 0 and points[1] % 2 == 0)):
        # *^V  triangle pointed up checked x,y
        #  V^
        self.point = 1
        self.draw_points = (((points[0]/2)*cell_w,(points[1]+1)*cell_h), #bottom left
                            (((points[0]/2)+1)*cell_w,(points[1]+1)*cell_h), # bottom right
                            (int(cell_w/2)+((points[0]/2)*cell_w),points[1]*cell_h)) # the point
      elif((points[0] % 2 == 1 and points[1] % 2 == 1)):
        # ^V   triangle pointed up checked x,y
        # V^*
        self.point = 1
        self.draw_points = (((((points[0]-1)/2)*cell_w)+int(cell_w/2),(points[1]+1)*cell_h), #bottom left
                            ((((points[0]+1)/2)*cell_w)+int(cell_w/2),(points[1]+1)*cell_h), # bottom right
                            (((points[0]+1)/2)*cell_w,points[1]*cell_h)) # the point
      elif(points[0] % 2 == 0 and points[1] % 2 == 1):
        #  ^V   triangle pointed down checked x,y
        # *V^
        self.point = 0
        self.draw_points = (((((points[0]/2)*cell_w)+int(cell_w/2)),(points[1]+1)*cell_h), # the point
                            (((((points[0])/2))*cell_w),(points[1])*cell_h), # top left
                            (((((points[0])/2)+1)*cell_w),(points[1])*cell_h)) # top right
      elif(points[0] % 2 == 1 and points[1] % 2 == 0):
        # ^V*   triangle pointed down checked x,y
        # V^
        self.point = 0
        self.draw_points = ((((points[0]+1)/2)*cell_w,(points[1]+1)*cell_h), # the point
                            (int(cell_w/2)+(((points[0]-1)/2)*cell_w),(points[1])*cell_h), # top left
                            (int(cell_w/2)+(((points[0]+1)/2)*cell_w),(points[1])*cell_h)) # top right
      else:
        print("This should never print")
        print(",".join(map(str,[points[0]%2==1,points[1]%2==0])))
      
      self.CollisionRect(cell_w,cell_h)

    def CollisionRect(self,w,h):
      x_min = None
      y_min = None
      for d in self.draw_points:
        if(y_min == None):
          x_min = d[0]
          y_min = d[1]
        else:
          if(x_min > d[0]):
            x_min = d[0]
          if(y_min > d[1]):
            y_min = d[1]
      self.rect = pygame.Rect(x_min,y_min,w,h)



