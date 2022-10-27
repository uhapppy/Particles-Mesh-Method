import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import time

from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

                


from  simulation.Simulation_1 import Simulation

def set_axes_equal(ax:plt.Axes):
    limits=np.array([ax.get_xlim3d(),ax.get_ylim3d(),ax.get_zlim3d()])
    origin=np.mean(limits,axis=1)
    radius = 0.5 *np.max(np.abs(limits[:,1]-limits[:,0]))
    _set_axes_radius(ax,origin,radius)


def _set_axes_radius(ax,origin,radius):
    x,y,z = origin
    ax.set_xlim3d([x-radius,x+radius])
    ax.set_ylim3d([y-radius,y+radius])
    ax.set_zlim3d([z-radius,z+radius])

    

fig = plt.figure()



def update(n):
    fig.clear()
    ax = fig.add_subplot(111, projection='3d')








    data_pos = np.load("data/position/itteration_"+str(n)+".npz")
    data_pos=np.transpose(data_pos["arr_0"])


    x = data_pos[0]
    y = data_pos[1]
    z = data_pos[2]

    xyz = np.vstack([x,y,z])
    density = stats.gaussian_kde(xyz)(xyz) 

    idx = density.argsort()
    x, y, z, density = x[idx], y[idx], z[idx], density[idx]

    ax.scatter(x, y, z, c=density , marker='.',s=1,cmap="magma")

    #ax.set_zlim(0,Simulation.largeur_mesh*Simulation.Size)      

    #plt.xlim(0,)
    #plt.ylim(0,)

    ax.set_box_aspect([1,1,1])
    set_axes_equal(ax)    


    #plt.gca().set_aspect(aspect='auto',adjustable='box',anchor='C',share=True)


    #xlim=ax.get_xlim()
    #ylim=ax.get_ylim()


    #if xlim[1] >= ylim[1]  and xlim[0] <= ylim[0]:
        #plt.ylim(xlim[0],xlim[1])

    #if xlim[1] >= ylim[1]  and xlim[0] >= ylim[0]:
        #plt.ylim(ylim[0],xlim[1])
        #plt.xlim(ylim[0],xlim[1])

    #if xlim[1] <= ylim[1]  and xlim[0] <= ylim[0]:
        #plt.ylim(xlim[0],ylim[1])
        #plt.xlim(xlim[0],ylim[1])

    #if xlim[1] <= ylim[1]  and xlim[0] >= ylim[0]:
        #plt.xlim(ylim[0],ylim[1])


    


    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    
    
    
    plt.savefig("screen_shot/screen_"+str(n)+".png",dpi=600)


for i in range(0,Simulation.itteration):
    t=time.time()
    update(i)
    print(i,time.time()-t)