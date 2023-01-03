from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: list = []
        self.users_collection: list = []

    def __check_if_user_exists_by_username(self, name):
        for user in self.users_collection:
            if user.username == name:
                return True

    def __check_if_movie_exists_by_title(self, title):
        for movie in self.movies_collection:
            if movie.title == title:
                return True

    def __check_if_movie_is_liked(self, username, movie_title):
        for user in self.users_collection:
            if user.username == username:
                for movie in user.movies_liked:
                    if movie.title == movie_title:
                        return True

    def __get_user_by_username(self, username):
        for user in self.users_collection:

            if user.username == username:
                return user

    def register_user(self, username: str, age: int):
        if self.__check_if_user_exists_by_username(username):
            raise Exception("User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        if not self.__check_if_user_exists_by_username(username):
            raise Exception("This user does not exist!")

        if self.__check_if_movie_exists_by_title(movie.title):
            raise Exception("Movie already added to the collection!")

        if username is not movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.append(movie)
        movie.owner.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if not self.__check_if_movie_exists_by_title(movie.title):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if username is not movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attr, new_value in kwargs.items():
            setattr(movie, attr, new_value)

        return f'{username} successfully edited {movie.title} movie.'

    def delete_movie(self, username: str, movie: Movie):
        if not self.__check_if_movie_exists_by_title(movie.title):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if username is not movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        # movie.owner.movies_owned.remove(movie)
        current_user = self.__get_user_by_username(username)
        current_user.movies_owned.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        if username is movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if self.__check_if_movie_is_liked(username, movie.title):
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        current_user = self.__get_user_by_username(username)
        current_user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        current_user = self.__get_user_by_username(username)
        if movie not in current_user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        current_user.movies_liked.remove(movie)
        movie.likes -= 1
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if len(self.movies_collection) == 0:
            return "No movies found."

        output = []
        for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
            output.append(movie.details())

        return '\n'.join(output)

    def __str__(self):
        output = []
        if len(self.users_collection) == 0:
            output.append("All users: No users.")
        else:
            output.append(f"All users: {', '.join([user.username for user in self.users_collection])}")

        if len(self.movies_collection) == 0:
            output.append("All movies: No movies.")
        else:
            output.append(f"All movies: {', '.join([movie.title for movie in self.movies_collection])}")

        return '\n'.join(output)