import random
import math
import numpy as np


class Distribution :

    def cube(size,offset) :
            x=(offset+random.random()*(size-(offset*2)-1))
            y=(offset+random.random()*(size-(offset*2)-1))
            z=(offset+random.random()*(size-(offset*2)-1))
            return np.array([[x,y,z],[0,0,0]])


    def sphere(size,offset) :
            rayon=random.random()*(size/2)-offset-1
            theta=random.random()*2*math.pi
            phi=random.random()*2*math.pi
            x=rayon*math.sin(phi)*math.cos(theta)+size/2
            y=rayon*math.sin(phi)*math.sin(theta)+size/2
            z=rayon*math.cos(phi)+size/2
            return np.array([[x,y,z],[0,0,0]])

    def galaxie(size,offset,angular_velocity) :
            rayon=random.random()*(size/2-offset-1)
            theta=random.random()*2*math.pi
            
            x=rayon*math.cos(theta)+size/2
            y=rayon*math.sin(theta)+size/2
            z=random.random()*2+size/2-2


            vx=-math.sin(theta)*angular_velocity*rayon
            vy=math.cos(theta)*angular_velocity*rayon
            vz=0
            return np.array([[x,y,z],[vx,vy,vz]])

