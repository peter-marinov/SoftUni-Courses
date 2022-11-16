class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        for current_album in self.albums:
            if current_album.name == album.name:
                return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        for current_album in self.albums:
            if current_album.name == album_name:
                if current_album.published:
                    return "Album has been published. It cannot be removed."

                self.albums.remove(current_album)
                return f"Album {album_name} has been removed."

        return f"Album {album_name} is not found."

    def details(self):
        output_string = f'Band {self.name}\n'
        for current_album in self.albums:
            output_string += current_album.details() + '\n'

        return output_string.strip()