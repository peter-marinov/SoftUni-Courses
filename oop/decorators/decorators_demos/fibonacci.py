class Fibonacci:
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n in self.cache:
            return self.cache[n]

        if n < 2:
            return 1

        result = self(n - 1) + self(n - 2)
        print(result)
        self.cache[n] = result

        return result

f = Fibonacci()
print(f(5))