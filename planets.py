import math

# Initializing variables
G = 6.67430e-11

# Escape velocity function
def calc_escape_velocity(mass, radius):
    vel = math.sqrt((2*G*mass)/(radius*1000))
    adj_vel = round((vel/1000), 2)
    return adj_vel

# Creating a tuple of planets used in analysis
planets = [("Mercury", 3.301e23, 2439.7), ("Venus", 4.87e24, 6051.8), ("Earth", 5.972e24, 6371), ("Mars", 6.42e23, 3389.5), ("Jupiter", 1.898e27, 69911)]

# Counters for classification types
low_count = 0
med_count = 0
high_count = 0

# Escape velocity for each planet within for loop
for name, mass, radius in planets:
    vel = calc_escape_velocity(mass, radius)
    if (vel < 6):
            classification = "Low"
            low_count = low_count+1
    elif (6 <= vel <= 15):
            classification = "Medium"
            med_count = med_count+1
    else:
          classification = "High"
          high_count = high_count+1
    print("The escape velocity for " + name + " is: " + str(vel) + " km/s. The classification is: " + classification + ".") # Printing escape velocities for planets

# Printing final summary
print(str(low_count) + ' planets fall into the "Low" category. ' + str(med_count) + ' planets fall into the "Medium" category. ' + str(high_count) + ' planet falls into the "High" category.')

