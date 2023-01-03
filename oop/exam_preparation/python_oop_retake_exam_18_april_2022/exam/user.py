class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: list = []
        self.movies_owned: list = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) == 0:
            raise ValueError("Invalid username!")

        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")

        self.__age = value

    def __str__(self):
        output = [f"Username: {self.username}, Age: {self.age}"]
        output.append('Liked movies:')
        if not self.movies_liked:
            output.append("No movies liked.")
        else:
            for movie in self.movies_liked:
                output.append(movie.details())

        output.append("Owned movies:")
        if not self.movies_owned:
            output.append("No movies owned.")
        else:
            for movie in self.movies_owned:
                output.append(movie.details())

        return '\n'.join(output)
