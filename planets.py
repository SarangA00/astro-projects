import math

# Initializing constants
G = 6.67430e-11

# Escape velocity function
def calc_escape_velocity(mass, radius):
    vel = math.sqrt((2*G*mass)/(radius*1000))
    adjVel = round((vel/1000), 2)
    return adjVel

# Creating a tuple of planets used in analysis
planets = [("Mercury", 3.301e23, 2439.7), ("Venus", 4.87e24, 6051.8), ("Earth", 5.972e24, 6371), ("Mars", 6.42e23, 3389.5), ("Jupiter", 1.898e27, 69911)]

# Escape velocity for each planet within for loop
for name, mass, radius in planets:
    vel = calc_escape_velocity(mass, radius)
    print("The escape velocity for " + name + " is: " + str(vel) + " km/s.") # Printing escape velocities for planets

