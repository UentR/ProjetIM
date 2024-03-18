import math
import numpy as np
import matplotlib.pyplot as plt

def orbite_calculator(*args):
    N = len(args)
    Dangle = []
    for i in range(N//2):
        Dangle.append(args[N//2+i]/args[i])
    Coeff = [1, -1, 1]
    def calculate_orbit_position(time):
        Theta = [Dangle[i]*time for i in range(N//2)]
        x = 0
        y = 0
        for i in range(N//2):
            x += args[i]*math.cos(Theta[i])*Coeff[i]
            y += args[i]*math.sin(Theta[i])*Coeff[i]
        return x, y

    return calculate_orbit_position

def main():
    R1 = 149
    R2 = 0.3
    R3 = 228
    V1 = 3
    V2 = 1.6
    V3 = 2.4
    lune_p2 = orbite_calculator(R2, R1, R3, V2, V1, V3)
    terre = orbite_calculator(R1, V1)
    lune_p1 = orbite_calculator(R2, R1, V2, V1)
    time = np.linspace(0, 13750, 100000)
    Pos = [lune_p1(t) for t in time]
    x, y = zip(*Pos)
    plt.plot(x, y)
    
    
    plt.rcParams['axes.facecolor'] = 'white'
    plt.rcParams['figure.facecolor'] = 'white'
    plt.show()

if __name__ == "__main__":
    main()