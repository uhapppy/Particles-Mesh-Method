import math



from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))


from integration.Integration_1 import Integration
from distribution.Distribution_1 import Distribution



class Simulation:

    G = 7.61422e-44 #  (anne lumiere)^3/(kg * anne^2)                            6.4743e-11   (N * m^2)/(kg)^2 = m^3 /(kg * s^2)

    dt = 0.003 #anner

    Size = 4 #anner lumiere

    largeur_mesh=64 #anner lumiere

    itteration = 500
    
    N_body = 40000

    mass = 0.3e44 #kg

    offset = 64 #espace entre la grille et la generationde body

    distribution = Distribution.galaxie

    integration = Integration.euler