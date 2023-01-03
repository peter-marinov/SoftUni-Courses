# class Person:
#     pass
#
#
# class PersonSingleton:
#     __instance = None
#
#     def __init__(self):
#         if self.__instance is None:
#             PersonSingleton.__instance = Person()
#         else:
#             raise Exception('Singleton cannot have more than one instance')


def singleton(cls):
    instance = [None]

    def wrapper(*args):
        if instance[0] is None:
            instance[0] = cls(*args)
        return instance[0]

    return wrapper()


@singleton
class Person:
    pass

