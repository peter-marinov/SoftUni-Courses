class custom_range_iterator:
    def __init__(self, cr):
        self.cr = cr
        self.next_value = self.cr.start

    def __next__(self):
        if self.next_value > self.cr.end:
            raise StopIteration

        value_to_return = self.next_value
        self.next_value += 1
        return value_to_return


class custom_range():
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __iter__(self):
        return custom_range_iterator(self)



cr = custom_range(1, 10)
ll = [1, 2, 3, 4, 5]

cr_iter = iter(cr)
ll_iter = iter(cr)

print(cr_iter)
print(ll_iter)

print('iter 1', next(cr_iter))
print('iter 1', next(cr_iter))
print('iter 1', next(cr_iter))
print('iter 2', next(ll_iter))
print('iter 2', next(ll_iter))