from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, nums):
        self.nums = nums

    @abstractmethod
    def execute(self, *args):
        pass
