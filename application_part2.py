import math
import numpy as np
import matplotlib.pyplot as plt

def orbite_calculator(R, V):
    Dangle = V/R
    def calculate_orbit_position(time):
        theta = Dangle*time
        x = R*math.cos(theta)
        y = R*math.sin(theta)
        return x, y
    return calculate_orbit_position

def main():
    # Définir les distances et les vitessesde la terre à chaque planète
    R_earth = 6378137 #m
    V_earth = 107219/3.6 #m/s
    R_mars = 3389500 #m
    V_mars = 24130 #m/s
    R_sun = 696340000 #m
    V_sun = 0 #m/s
    # Créer une fonction pour chaque planète
    earth_orbit_calculator = orbite_calculator(R_earth, V_earth)
    mars_orbit_calculator = orbite_calculator(R_mars, V_mars)
    sun_orbit_calculator = orbite_calculator(R_sun, V_sun)

    time = np.linspace(0, 1570, 100000)

    # Calculer la position de chaque planète à chaque instant
    earth_pos = [earth_orbit_calculator(t) for t in time]
    mars_pos = [mars_orbit_calculator(t) for t in time]
    sun_pos = [sun_orbit_calculator(t) for t in time]

    # Tracer la trajectoire de chaque planète
    for planet_pos, label in zip([earth_pos, mars_pos, sun_pos], ["Terre", "Mars", "Soleil"]):
        x, y = zip(*planet_pos)
        plt.plot(x, y, label=label)

    plt.rcParams['axes.facecolor'] = 'white'
    plt.rcParams['figure.facecolor'] = 'white'
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()