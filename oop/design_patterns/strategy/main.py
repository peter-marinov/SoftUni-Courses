from design_patterns.strategy.ascending_sorter import AscendingSorter

nums = [5, 2, 3, 4, 1]

asc_sorter = AscendingSorter(nums)
print(asc_sorter.sort())