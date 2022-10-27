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




ax = fig.add_subplot(111, projection='3d')



data_pos = np.load("data/position/itteration_0.npz")
data_pos=np.transpose(data_pos["arr_0"])

print(data_pos)

x = data_pos[0]
y = data_pos[1]
z = data_pos[2]

xyz = np.vstack([x,y,z])
density = stats.gaussian_kde(xyz)(xyz) 

idx = density.argsort()
x, y, z, density = x[idx], y[idx], z[idx], density[idx]

ax.scatter(x, y, z, c=density , marker='.',s=1,cmap="cool")

plt.xlim(0,Simulation.largeur_mesh*Simulation.Size)
plt.ylim(0,Simulation.largeur_mesh*Simulation.Size)
ax.set_zlim(0,Simulation.largeur_mesh*Simulation.Size)

#ax.set_box_aspect([1,1,1])
#set_axes_equal(ax)



ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
    
plt.show()