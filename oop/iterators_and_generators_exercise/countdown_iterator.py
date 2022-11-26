class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.current_count = count

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_count >= 0:
            value_to_return = self.current_count
            self.current_count -= 1
            return value_to_return
        raise StopIteration

iterator = countdown_iterator(10)

for item in iterator:
    print(item, end=" ")