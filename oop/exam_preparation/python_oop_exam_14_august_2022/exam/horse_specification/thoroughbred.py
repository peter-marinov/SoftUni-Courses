from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        speed_increase = 3
        if self.speed + speed_increase > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        else:
            self.speed += speed_increase
