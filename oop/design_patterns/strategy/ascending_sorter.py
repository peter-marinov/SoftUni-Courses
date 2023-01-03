from design_patterns.strategy.sorter import Sorter


class AscendingSorter(Sorter):
    def __init__(self, nums):
        super().__init__(nums)
        self._strategy = lambda x: x
