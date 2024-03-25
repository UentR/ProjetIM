import math
import numpy as np
import matplotlib.pyplot as plt

import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
myapp = App(root)
myapp.mainloop()

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