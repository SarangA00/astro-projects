import math

# Initializing constants
G = 6.67430e-11

# Getting user data
mass = float(input("Enter the planetary mass (kg): "))
radius = float(input("Enter the planetary radius (km): "))

# Main calculation function
def calc_escape_velocity(mass, radius):
    vel = math.sqrt((2*G*mass)/(radius*1000))
    adjVel = round((vel/1000), 2)
    print("The escape velocity for the planet is: " + str(adjVel) + " km/sec.")

# Mars test case
calc_escape_velocity(6.39e23, 3389.5)

# Calling function
calc_escape_velocity(mass, radius)