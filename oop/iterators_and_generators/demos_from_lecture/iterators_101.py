'''
__iter__() - internal dunder method in class
iter() - external from class function, that calls __iter__()
'''

print(' --- With for loop ---')
ll = [1, 2, 3, 4, 5]
for x in ll:
    print(x)

print(' --- Manual ---')
ll_iter = iter(ll)
print(ll_iter)
print(next(ll_iter)) # get next value
print(next(ll_iter))
print(next(ll_iter))
print(next(ll_iter))
print(next(ll_iter))

print(' --- With while loop ---')
ll_iter = iter(ll)

while True:
    try:
        value = next(ll_iter)
        print(value)
    except StopIteration:
        print('Stop iteration raised')
        break
