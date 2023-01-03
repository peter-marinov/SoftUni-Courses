from project.hardware.hardware import Hardware
from math import floor


class PowerHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, 'Power', floor(capacity * 0.25), floor(memory * 1.75))
