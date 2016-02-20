import sys
import Cell
import random
import pygame 
import pygame.gfxdraw
import GasJet

class Genome():
    """description of class"""
    def __init__(self,surface,tri_w,tri_h,color):
      self.surface = surface
      #self.surface.set_colorkey((125,125,125))
      self.surface.fill((125,125,125))
      self.north_jet = GasJet.GasJet('n',(125,125,125),(250,250,250))
      (surface_w,surface_h) = surface.get_size()
      self.tri_x = (2*int(surface_w/tri_w))-1
      self.tri_y = int(surface_h/tri_h)
      self.tri_w = tri_w
      self.tri_h = tri_h
      self.loaded_rect = None
      seed = Cell.Cell((int(self.tri_x/2),int(self.tri_y/2)),color,tri_w,tri_h)
      self.alive_array = [seed]
      self.grid = [[0 for y in range(self.tri_y)] for x in range(self.tri_x)]
      self.grid[seed.index[0]][seed.index[1]] = 1
      self.growth_array = dict()
      self.collision_list = [(seed.rect,seed.index[1])]
      self.UpdateGrowthHash(seed)
      self.filename = 'test.bmp'
      self.DrawAndSave()
      
    def UpdateGrowthHash(self,cell):
      if(self.growth_array.has_key(str(cell.index))):
        del self.growth_array[str(cell.index)]
     
      #print "\t".join(map(str,[cell.index,len(self.grid),len(self.grid[0])]))
      if(cell.index[0]-1 >= 0 and self.grid[cell.index[0]-1][cell.index[1]] == 0):
        new = Cell.Cell((cell.index[0]-1,cell.index[1]),self.ColorGenerate(cell),self.tri_w,self.tri_h)
        self.growth_array[str(new.index)] = new
      if(cell.index[0]+1 < self.tri_x and self.grid[cell.index[0]+1][cell.index[1]] == 0):
        new = Cell.Cell((cell.index[0]+1,cell.index[1]),self.ColorGenerate(cell),self.tri_w,self.tri_h)
        #new = (cell.index[0]+1,cell.index[1])
        self.growth_array[str(new.index)] = new
      
      if(cell.point == 1): # triangle pointed up
        if(cell.index[1]+1 < self.tri_y and self.grid[cell.index[0]][cell.index[1]+1] == 0):
          new = Cell.Cell((cell.index[0],cell.index[1]+1),self.ColorGenerate(cell),self.tri_w,self.tri_h)
          #new = (cell.index[0],cell.index[1]+1)
          self.growth_array[str(new.index)] = new
      else:
        if(cell.index[1]-1 >= 0 and self.grid[cell.index[0]][cell.index[1]-1] == 0):
          new = Cell.Cell((cell.index[0],cell.index[1]-1),self.ColorGenerate(cell),self.tri_w,self.tri_h)
          #new = (cell.index[0],cell.index[1]-1)
          self.growth_array[str(new.index)] = new 

    def AddCell(self):
     growth_cell = random.choice(self.growth_array.values())
     #growth_color = (random.randint(0,250),random.randint(0,250),random.randint(0,250))
     #growth_cell = Cell.Cell(growth_point,growth_color,self.tri_w,self.tri_h)
     self.alive_array.append(growth_cell)
     self.grid[growth_cell.index[0]][growth_cell.index[1]] = 1
     self.UpdateGrowthHash(growth_cell)
     self.UpdateCollisionRectArray(growth_cell)
     self.DrawAndSave()

    def DrawAndSave(self):
      for c in self.alive_array:
        pygame.gfxdraw.filled_polygon(self.surface,c.draw_points,c.color)
      pygame.image.save(self.surface,self.filename)
      self.loaded = pygame.image.load(self.filename)
      self.loaded.set_colorkey((125,125,125))
      self.loaded = pygame.Surface.convert(self.loaded)
      #self.loaded = pygame.transform.scale(self.loaded,(500,500))
      if(self.loaded_rect == None):
        self.loaded_rect = self.loaded.get_rect()
      print(','.join(map(str,[self.loaded_rect.width,self.loaded_rect.height])))

    def ColorGenerate(self,gen_cell):
      red = gen_cell.color[0]
      green = gen_cell.color[1]
      blue = gen_cell.color[2]
      red_delta = random.randint(0,21)-10
      green_delta = random.randint(0,21)-10
      blue_delta = random.randint(0,21)-10
      red = self.ColorCircle(red+red_delta)
      green = self.ColorCircle(green+green_delta)
      blue = self.ColorCircle(blue+blue_delta)
      if(red == 125 and blue == 125 and green == 125):
        return self.ColorGenerate(gen_cell)
      return(red,green,blue)  

    def ColorCircle(self,value):
      if(value < 0):
        return 250+value;
      if(value > 250):
        return value-250
      return value
    
    def UpdateCollisionRectArray(self,cell):
      new_collision_list = []
      toAdd = cell.rect.copy()
      for r,y in self.collision_list:
        if(cell.index[1] == y and toAdd.colliderect(r)):
          toAdd = toAdd.union(r)
          print("Merge")
        else:
          new_collision_list.append((r,y))
      new_collision_list.append((toAdd,cell.index[1]))
      self.collision_list = new_collision_list
      print(len(new_collision_list))
      self.WriteCollision()

    def rotate_center(self,angle):
      rotated_image = pygame.transform.rotozoom(self.loaded,angle,1)
      rotated_rect = self.loaded_rect.copy()
      rotated_rect.center = rotated_image.get_rect().center
      rotated_image = rotated_image.subsurface(rotated_rect).copy()
      self.loaded = rotated_image
      self.loaded_rect = rotated_rect

    def collide(self,rect):
      dx = self.loaded_rect.left
      dy = self.loaded_rect.top
      for r,y in self.collision_list:
        d_rect = pygame.Rect(r.left+dx,r.top+dy,r.width,r.height)
        if(d_rect.colliderect(rect)):
          return True
      return False

    def move(self,speed):
      self.loaded_rect = self.loaded_rect.move(speed)
      #new_collision_list = []
      #for r,y in self.collision_list:
      #  new_collision_list.append((r.move(speed),y))
      #self.collision_list = new_collision_list
    def WriteCollision(self):
      dx = self.loaded_rect.top
      dy = self.loaded_rect.left
      for r,y in self.collision_list:
        print ",".join(map(str,[r.top+dy,r.left+dx,r.bottom+dy,r.right+dx]))
