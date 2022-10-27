

import math
import numpy as np
import random
import time


from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

                
from  body.Body_1 import Body
from  mesh.Mesh_1 import Mesh
from  simulation.Simulation_1 import Simulation





itteration=Simulation.itteration
dt=Simulation.dt

mesh = Mesh(Simulation.largeur_mesh) 





for i in range(0,Simulation.N_body): # create  bodies

    pos_speed=Simulation.distribution(Simulation.Size*Simulation.largeur_mesh,Simulation.offset,math.pi/1.8)
    
    Body(Simulation.mass,10,pos_speed[0],pos_speed[1])

    







def update(mesh,dt,itteration) :
        mesh.Density_Grid = np.zeros(shape = (mesh.Size,mesh.Size,mesh.Size) , dtype = np.float64)
        

        mesh.Green_Grid = np.zeros(shape = (mesh.Size,mesh.Size,mesh.Size) , dtype = np.float64)


        mesh.Potential_Grid = np.zeros(shape = (mesh.Size,mesh.Size,mesh.Size) , dtype = np.float64)


        mesh.acc_x=np.zeros(shape = (mesh.Size,mesh.Size,mesh.Size) , dtype = np.float64)
        mesh.acc_y=np.zeros(shape = (mesh.Size,mesh.Size,mesh.Size) , dtype = np.float64)
        mesh.acc_z=np.zeros(shape = (mesh.Size,mesh.Size,mesh.Size) , dtype = np.float64)


        for body in Body.all_body:
            mesh.assign_density(body)


        mesh.create_green_func() # create the green function for each cell
        mesh.find_pot() # find the potential for each cell
        mesh.find_acc() # find the accelerating grid for each cell


 

        
        position=[]
        int_body=np.array([])


        for body in Body.all_body: # find the acceleration for each body et update la position
            
            body.get_acceleration(mesh.acc_x,mesh.acc_y,mesh.acc_z) 
            body.update_position(dt)
            if body.position[0]>mesh.Size*mesh.delta_size-mesh.delta_size or body.position[0]<0 or body.position[1]>mesh.Size*mesh.delta_size-mesh.delta_size or body.position[1]<0 or body.position[2]>mesh.Size*mesh.delta_size-mesh.delta_size or body.position[2]<0 :
                continue
            else :
                int_body = np.append(int_body,body)
                position.append(body.position)
                

        print(len(position))
        Body.all_body=int_body
        
        
        np.savez("data/position/itteration_"+str(itteration),np.array(position))

for i in range(0,itteration):
    temps=time.time()
    update(mesh,dt,i)
    print(i,time.time()-temps)