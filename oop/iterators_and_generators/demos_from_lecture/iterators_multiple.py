ll = [1, 2, 3, 4, 5]

ll_iter1 = iter(ll)
ll_iter2 = iter(ll)

print('iter 1', next(ll_iter1))
print('iter 1', next(ll_iter1))
print('iter 1', next(ll_iter1))
print('iter 2', next(ll_iter2))
print('iter 2', next(ll_iter2))