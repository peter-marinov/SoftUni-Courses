from project.cat import Cat


class Tomcat(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, 'Male')
        self.name = name
        self.age = age

    def make_sound(self):
        return f'Hiss'