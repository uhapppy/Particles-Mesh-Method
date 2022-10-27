import numpy as np
import math

from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

                


from  simulation.Simulation_1 import Simulation



class Body :

   all_body=[]

   def __init__(self, mass, radius, pos,speed ) :

        
        self.position = pos
        self.speed = speed
        self.acceleration = np.array([0.,0.,0.])

        self.radius = radius
        self.mass = mass

        Body.all_body.append(self)





   
         

   def get_acceleration(self,acc_x,acc_y,acc_z) :

      
         delta_size=Simulation.Size

         i=math.floor(self.position[0]/delta_size)
         j=math.floor(self.position[1]/delta_size)
         k=math.floor(self.position[2]/delta_size)

         x_center = i*delta_size+(delta_size/2)
         y_center = j*delta_size+(delta_size/2)
         z_center = k*delta_size+(delta_size/2)

         dx = (self.position[0] - x_center)/delta_size
         dy = (self.position[1] - y_center)/delta_size
         dz = (self.position[2] - z_center)/delta_size

         tx = 1 - dx
         ty = 1 - dy
         tz = 1 - dz






         self.acceleration[0] = acc_x[i][j][k] * tx * ty * tz + acc_x[i+1][j][k] * dx * ty * tz + acc_x[i][j+1][k] * tx * dy * tz + acc_x[i][j][k+1] * tx * ty * dz + acc_x[i+1][j+1][k] * dx * dy * tz + acc_x[i+1][j][k+1] * dx * ty * dz + acc_x[i][j+1][k+1] * tx * dy * dz + acc_x[i+1][j+1][k+1] * dx * dy * dz
         self.acceleration[1] = acc_y[i][j][k] * tx * ty * tz + acc_y[i+1][j][k] * dx * ty * tz + acc_y[i][j+1][k] * tx * dy * tz + acc_y[i][j][k+1] * tx * ty * dz + acc_y[i+1][j+1][k] * dx * dy * tz + acc_y[i+1][j][k+1] * dx * ty * dz + acc_y[i][j+1][k+1] * tx * dy * dz + acc_y[i+1][j+1][k+1] * dx * dy * dz
         self.acceleration[2] = acc_z[i][j][k] * tx * ty * tz + acc_z[i+1][j][k] * dx * ty * tz + acc_z[i][j+1][k] * tx * dy * tz + acc_z[i][j][k+1] * tx * ty * dz + acc_z[i+1][j+1][k] * dx * dy * tz + acc_z[i+1][j][k+1] * dx * ty * dz + acc_z[i][j+1][k+1] * tx * dy * dz + acc_z[i+1][j+1][k+1] * dx * dy * dz



   def update_position(self,dt) :
         

      self.speed=Simulation.integration(self.speed,dt,self.acceleration)
      self.position=Simulation.integration(self.position,dt,self.speed)


