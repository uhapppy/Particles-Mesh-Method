import numpy as np
import math



from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

                
from  body.Body_1 import Body
from  simulation.Simulation_1 import Simulation






#class mesh
# le mesh  est notre espace ou se deroule la simulation 
# l'espace est un cube de coter Size on veut diviser l'espace de maniere 
# discrete pour se faire on divise l'espace en plus petit cube de longueur 1
# chauqe cube aura une densiter assigner a celui-ci selon le nombre d'object
# a l'interieur ainsi qua l'interieur de c'est voisin (cloud in cell)

#la position des body doivent etre seulemnt positive x>0 ,y>0 , z>0

class Mesh :

    

    def __init__(self,Size,delta_size=Simulation.Size) :

        self.Size = Size

        self.delta_size = delta_size

        self.Density_Grid = np.zeros(shape = (Size,Size,Size) , dtype = np.float64)
        

        self.Green_Grid = np.zeros(shape = (Size,Size,Size) , dtype = np.float64)


        self.Potential_Grid = np.zeros(shape = (Size,Size,Size) , dtype = np.float64)


        self.acc_x=np.zeros(shape = (Size,Size,Size) , dtype = np.float64)
        self.acc_y=np.zeros(shape = (Size,Size,Size) , dtype = np.float64)
        self.acc_z=np.zeros(shape = (Size,Size,Size) , dtype = np.float64)





    def assign_density(self,body):



        i=math.floor(body.position[0]/self.delta_size)
        j=math.floor(body.position[1]/self.delta_size)
        k=math.floor(body.position[2]/self.delta_size)

        x_center = i*self.delta_size+(self.delta_size/2)
        y_center = j*self.delta_size+(self.delta_size/2)
        z_center = k*self.delta_size+(self.delta_size/2)

        dx = (body.position[0] - x_center)/self.delta_size
        dy = (body.position[1] - y_center)/self.delta_size
        dz = (body.position[2] - z_center)/self.delta_size

        tx = 1 - dx
        ty = 1 - dy
        tz = 1 - dz





        self.Density_Grid[i][j][k] += body.mass * tx * ty * tz

        self.Density_Grid[i+1][j][k] += body.mass * dx * ty * tz
        self.Density_Grid[i][j+1][k] += body.mass * tx * dy * tz
        self.Density_Grid[i][j][k+1] += body.mass * tx * ty * dz

        self.Density_Grid[i+1][j+1][k] += body.mass * dx * dy * tz
        self.Density_Grid[i+1][j][k+1] += body.mass * dx * ty * dz
        self.Density_Grid[i][j+1][k+1] += body.mass * tx * dy * dz 

        self.Density_Grid[i+1][j+1][k+1] += body.mass * dx * dy * dz



    def create_green_func(self): #create the green function for each cell
        for i in range(0, self.Size):
            for j in range(0, self.Size):
                for k in range(0, self.Size):
                    if i==0 and j==0 and k==0 :
                        self.Green_Grid[i][j][k] = 0
                    else :
                        
                        self.Green_Grid[i][j][k] = -(1/((math.sin(math.pi*i/self.Size)**2) + (math.sin(math.pi*j/self.Size)**2) + (math.sin(math.pi*k/self.Size)**2)))*(4*math.pi*Simulation.G)



    def find_pot(self):
        fft_density = np.fft.fftn(self.Density_Grid)
        fft_potential = np.multiply(fft_density,self.Green_Grid)
        real_potential = np.fft.ifftn(fft_potential)
        self.Potential_Grid = real_potential.real

    def find_acc(self):
        for i in range(1,self.Size-1):
            for j in range(1,self.Size-1):
                for k in range(1,self.Size-1):
                    self.acc_x[i][j][k] = -(self.Potential_Grid[i+1][j][k] - self.Potential_Grid[i-1][j][k])/2
                    self.acc_y[i][j][k] = -(self.Potential_Grid[i][j+1][k] - self.Potential_Grid[i][j-1][k])/2
                    self.acc_z[i][j][k] = -(self.Potential_Grid[i][j][k+1] - self.Potential_Grid[i][j][k-1])/2
