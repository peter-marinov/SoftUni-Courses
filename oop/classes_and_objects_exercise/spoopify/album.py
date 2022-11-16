class Album:
    def __init__(self, name: str, *album_songs):
        self.name = name
        self.album_songs = album_songs
        self.published = False
        self.songs = []
        for album_song in album_songs:
            self.songs.append(album_song)

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        if song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if self.published:
            return "Cannot remove songs. Album is published."

        for current_song in self.songs:
            if song_name == current_song.name:
                self.songs.remove(current_song)
                return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        output_string = f'Album {self.name}\n'
        for current_song in self.songs:
            output_string += '== ' + current_song.get_info() + '\n'

        return output_string
