import Particle
import sys
import math

p = Particle.Particle((50,50),math.pi/4,2,10)

for i in range(10):
  p.vector_update();
