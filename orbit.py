# Gathering user data
orbitalRadius = input("Please enter the orbital radius in astronomical units: ")

# Calculating orbita period with user data
orbitalPeriod = round((float(orbitalRadius)**1.5),2)
print("The orbital period is " + str(orbitalPeriod) + " years")

