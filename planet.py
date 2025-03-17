class planet:
    def __init__(self, name: str, startPos: list[float, float], initialVelocity: list[float, float], mass: float, radius: float, color: tuple[int, int, int]):
        self.name = name
        self.pos = startPos
        self.vel = initialVelocity
        self.mass = mass
        self.radius = radius
        self.color = color

    def Move(self, deltaTime: float, acc: tuple[float, float]):
        self.vel[0] += acc[0] * deltaTime
        self.vel[1] += acc[1] * deltaTime

        self.pos[0] += self.vel[0] * deltaTime
        self.pos[1] += self.vel[1] * deltaTime