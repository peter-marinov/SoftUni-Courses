class PostdreSQL:
    ...


class StudentsController:
    def __init__(self):
        self.db = PostdreSQL()


class StudentsController2:
    def __init__(self, db):
        self.db = db


# Production:
sc = StudentsController() # works with PostgreSQL
sc2 = StudentsController2(PostdreSQL())
# Testing following

class FakeDb:
    '''
    Saves data in a list
    '''
    pass

sc = StudentsController() # works with PostqreSQL
sc2 = StudentsController2(FakeDb()) # works with lists
# Make actual database queris to the DB