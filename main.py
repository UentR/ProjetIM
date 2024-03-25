import math
import numpy as np
import matplotlib.pyplot as plt

from dataclasses import dataclass

@dataclass
class Planete:
    Radius: float
    Speed: float
    Angle: float = 0
    def __post_init__(self):
        self.Angle = self.Speed/self.Radius

def orbite_calculator(*args):
    N = len(args)
    Dangle = np.zeros(N)
    for i in range(N):
        Dangle[i] = args[i].Angle
    def calculate_orbit_position(time):
        time = np.repeat(time, N, axis=0).reshape(N, time.shape[0])
        print(time)
        Theta = time*Dangle[:, None]
        COS = np.cos(Theta)
        SIN = np.sin(Theta)
        x = 0
        y = 0
        Coeff = 1
        for i in range(N):
            x += args[i].Radius*COS[i]*Coeff
            y += args[i].Radius*SIN[i]*Coeff
            Coeff *= -1
        return x, y

    return calculate_orbit_position

def main():
    Terre = Planete(149, 2.735*4)
    Lune = Planete(0.3, 1.6)
    Mars = Planete(228*3, 1.4)
    lune_p2 = orbite_calculator(Lune, Terre, Mars)
    terre_P1 = orbite_calculator(Terre, Mars)
    lune_p1 = orbite_calculator(Lune, Terre)
    time = np.linspace(0, 2055*5, 100000)
    x, y = lune_p2(time)
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.plot(x, y)
    # remove the axis
    # ax.axis('off')
    # set the aspect of the plot to be equal
    ax.set_aspect('equal', adjustable='datalim')
    
    
    plt.show()
    fig.savefig("terre_p1.png")



if __name__ == "__main__":
    main()