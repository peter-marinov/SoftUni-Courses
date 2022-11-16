class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.memory_used = 0
        self.is_on = False
        self.apps = []

    def power(self):
        self.is_on = not self.is_on

    def install(self, app, app_memory):
        if not self.is_on:
            return f'Turn on your phone to install {app}'

        if self.calculate_memory_left() < app_memory:
            return f'Not enough memory to install {app}'

        self.apps.append(app)
        self.memory_used += app_memory
        return f'Installing {app}'

    def status(self):
        total_apps_count = len(self.apps)
        memory_left = self.calculate_memory_left()
        return f"Total apps: {total_apps_count}. Memory left: {memory_left}"

    def calculate_memory_left(self):
        return self.memory - self.memory_used

smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())