# Creating planets dictionary
planets = {}

with open("results.txt") as f:
      for line in f:
        name, vel, classif = line.strip().split(",") # Splitting the lines to extract induvidual data points
        vel = float(vel)
        planets[classif] = planets.get(classif, 0) + 1

for category, count in planets.items():
    print(str(count) + " planets fall into the " + category + " category.")