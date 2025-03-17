import planet

def Read_Planet_Data(fileName, scaleFactor, timeScale) -> list[planet.planet]:
    planets = []
    cosmicScaleFactor = 1.0

    with open(fileName, "r") as file:
        for line in file:
            if line.startswith("#") or line.strip() == "":
                continue
            if line.startswith("%"):
                cosmicScaleFactor = float(line.strip()[1:])  
                continue         

            data = line.strip().split(",")

            dis = 0
            if line.startswith("$"):
                dis = float(data[10]) / scaleFactor

            name = data[0].strip()
            x, y = float(data[1]), float(data[2]) + dis
            vx, vy = float(data[3]), float(data[4])
            mass = (float(data[5]) / 212600 / scaleFactor) * timeScale
            radius = float(data[6]) * cosmicScaleFactor / scaleFactor
            color = (int(data[7]), int(data[8]), int(data[9]))

            planets.append(planet.planet(name, [x, y], [vx * timeScale, vy * timeScale], mass, radius, color))

    return planets