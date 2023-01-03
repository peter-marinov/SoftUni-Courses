from project.software.software import Software
from math import floor


class LightSoftware(Software):
    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, 'Light', floor(capacity_consumption * 1.5), floor(memory_consumption * 0.5))

