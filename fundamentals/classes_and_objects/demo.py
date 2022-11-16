# def say_hi(name):
#     print(f'Hello {name}')
#
# print(say_hi('Gosho'))
# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def say_hello(self):
#         return f'Hello {self.first_name} {self.last_name}'
#
#
# ivan = Person('Ivan', 'Ivanov')
# gosho = Person('Gosho', 'Georgiev')
# print(ivan.say_hello())
# print(gosho.last_name)

# class Person:
#     pass
#
# gosho = Person()
# gosho.name = 'Gosho Ivanov'
#
# print(gosho.name)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# ivan = Person('Ivan', 32)
# ivan.age += 5
# print(ivan.age)

class Test:
    pi = 3.14

    def __init__(self):
        pass

test = Test()
test.pi += 10
print(test.pi)