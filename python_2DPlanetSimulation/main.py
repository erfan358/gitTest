import pygame as pg
import planet
import GameTime as time
import physics
import FileReader as reader

pg.init()
time.InitializeTime()
screen = pg.display.set_mode((1280, 1024))

isRunning = True

timeScale: float = 5
scaleFactor = 5

# every 1 unit is 212,600m for radius
# distance between the moon and the earth is 1,808 units
#planets = reader.Read_Planet_Data("senarios/earth_moon_orbit.txt", scaleFactor, timeScale)
planets = reader.Read_Planet_Data("senarios/highDensity3Bodies.txt", scaleFactor, timeScale)

for p in planets:
    p.orbit_path = []

def Physics():
    for planet in planets:
        planetAcc = [0, 0]
        for other_planet in planets:
            if planet.name == other_planet.name:
                continue
            
            planetAcc[0] += physics.Calculate_Gravity(planet, other_planet)[0] * timeScale
            planetAcc[1] += physics.Calculate_Gravity(planet, other_planet)[1] * timeScale
        planet.Move(time.delta_time, planetAcc)
        


lastSampleTime = 0
samplingRate = 1 * timeScale
def CalculateOrbit():
    samplingLimit = 5000
    global lastSampleTime, samplingRate
    if time.Time < lastSampleTime + 1 / samplingRate:
        return
    
    lastSampleTime = time.Time
    for planet in planets:
        planet.orbit_path.append((int(planet.pos[0]), int(planet.pos[1])))
        
        if len(planet.orbit_path) > samplingLimit:  
            planet.orbit_path.pop(0)


def RenderPass():
    screen.fill((0, 0, 0))

    for planet in planets:
        if len(planet.orbit_path) > 1:
            pg.draw.lines(screen, planet.color, False, planet.orbit_path, 1)

    for planet in planets:
        pg.draw.circle(screen, planet.color, (planet.pos[0], planet.pos[1]), planet.radius)    
    pg.display.flip()


while isRunning:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRunning = False

    time.Calculate_DeltaTime()
    Physics()
    CalculateOrbit()
    RenderPass()


pg.quit()