class func_logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'{self.func.__name__} was called with {args} and {kwargs}')
        return self.func(*args, **kwargs)


@func_logger
def say_hi(name, country):
    return f'hello {name} from {country}'


@func_logger
def say_bye():
    return 'goodbye'

print(say_hi('Pesho', 'Bulgaria'))
print(say_bye())