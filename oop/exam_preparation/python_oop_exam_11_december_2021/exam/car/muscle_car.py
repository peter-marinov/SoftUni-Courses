from project.car.car import Car


class MuscleCar(Car):
    MIN_SPEED = 250
    MAX_SPEED = 450

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)
        self.is_taken = False

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if value < self.MIN_SPEED or value > self.MAX_SPEED:
            raise ValueError(f"Invalid speed limit! Must be between {self.MIN_SPEED} and {self.MAX_SPEED}!")

        self.__speed_limit = value


