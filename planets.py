import math

# Initializing variables
G = 6.67430e-11

# Escape velocity function
def calc_escape_velocity(mass, radius):
    vel = math.sqrt((2*G*mass)/(radius*1000))
    adj_vel = round((vel/1000), 2)
    return adj_vel

# Counters for classification types
low_count = 0
med_count = 0
high_count = 0

# Opening text file containing planet data
with open("planet_data.txt") as f, open("results.txt", "w") as out:
      for line in f:
        name, mass, radius = line.strip().split(",") # Splitting the lines to extract induvidual data points
        mass = float(mass)
        radius = float(radius)

        # Escape velocity for each planet within for loop
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
        out.write(name + "," + str(vel) + "," + classification + "\n")
# Printing final summary
print(str(low_count) + ' planets fall into the "Low" category. ' + str(med_count) + ' planets fall into the "Medium" category. ' + str(high_count) + ' planet falls into the "High" category.')

