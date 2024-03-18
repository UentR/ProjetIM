import math
import numpy as np
import matplotlib.pyplot as plt

def orbite_calculator(R1, R2, R3, V1, V2, V3):
    Dangle1 = V1/R1
    Dangle2 = V2/R2
    Dangle3 = V3/R3
    def calculate_orbit_position(time):
        theta1 = Dangle1*time
        theta2 = Dangle2*time
        theta3 = Dangle3*time
        x = R2*math.cos(theta2) - R1*math.cos(theta1) + R3*math.cos(theta3)
        y = R2*math.sin(theta2) - R1*math.sin(theta1) + R3*math.sin(theta3)
        return x, y

    return calculate_orbit_position

def main():
    R1 = 149
    R2 = 10
    R3 = 384
    V1 = 3
    V2 = 9.5
    V3 = 1.55
    orbit_calculator = orbite_calculator(R1, R2, R3, V1, V2, V3)
    time = np.linspace(0, 1570, 100000)
    Pos = [orbit_calculator(t) for t in time]
    x, y = zip(*Pos)
    plt.plot(x, y, label="Orbite de la Lune autour du Soleil")
    plt.rcParams['axes.facecolor'] = 'white'
    plt.rcParams['figure.facecolor'] = 'white'
    plt.show()

if __name__ == "__main__":
    main()