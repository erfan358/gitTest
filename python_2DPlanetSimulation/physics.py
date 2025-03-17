import math
import planet

G = 6.67408e-11 / 212600

def Calculate_Gravity(planet1: planet, planet2: planet) -> tuple[float, float]:
    dx = planet2.pos[0] - planet1.pos[0]
    dy = planet2.pos[1] - planet1.pos[1]

    r = math.sqrt(dx**2 + dy**2)

    if r == 0:  # Prevent division by zero
            return (0, 0)

    F = G * (planet1.mass * planet2.mass) / r**2

    Fx = F * (dx / r)
    Fy = F * (dy / r)

    AccX = Fx / planet1.mass
    AccY = Fy / planet1.mass

    return (AccX, AccY)