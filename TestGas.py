import Particle
import sys

p = Particle.Particle((50,50),.1,2,10)

for i in range(10):
  p.vector_update();
