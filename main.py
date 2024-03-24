import math
import numpy as np
import matplotlib.pyplot as plt

def orbite_calculator(*args):
    N = len(args)//2
    Dangle = np.zeros(N)
    for i in range(N):
        Dangle[i] = args[N+i]/args[i]
    def calculate_orbit_position(time):
        time = np.repeat(time, N, axis=0).reshape(N, time.shape[0])
        Theta = time*Dangle[:, None]
        COS = np.cos(Theta)
        SIN = np.sin(Theta)
        x = 0
        y = 0
        Coeff = 1
        for i in range(N):
            x += args[i]*COS[i]*Coeff
            y += args[i]*SIN[i]*Coeff
            Coeff *= -1
        return x, y

    return calculate_orbit_position

def main():
    R1 = 149
    R2 = 0.3
    R3 = 228*3
    V1 = 2.735*4
    V2 = 1.6
    V3 = 1.4
    # lune_p2 = orbite_calculator(R2, R1, R3, V2, V1, V3)
    terre_P1 = orbite_calculator(R1, R3, V1, V3)
    lune_p1 = orbite_calculator(R2, R1, V2, V1)
    time = np.linspace(0, 2055*3, 100000)
    x, y = terre_P1(time)
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.plot(x, y)
    # remove the axis
    ax.axis('off')
    # set the aspect of the plot to be equal
    ax.set_aspect('equal', adjustable='datalim')
    
    
    fig.show()
    fig.savefig("terre_p1.png")

if __name__ == "__main__":
    main()