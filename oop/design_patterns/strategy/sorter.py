from abc import ABC, abstractmethod


class Sorter(ABC):
    _strategy = None

    def __init__(self, nums):
        self.nums = nums

    def sort(self):
        return sorted(self.nums, key=self._strategy)