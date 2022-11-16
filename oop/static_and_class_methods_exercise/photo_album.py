from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = self.build_photos()

    def build_photos(self):
        result = []
        for _ in range(self.pages):
            result.append([])
        return result

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        for row, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PHOTOS_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {row + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        page_sep = '-' * 11
        result = page_sep + '\n'
        for page in self.photos:
            page_str = ' '.join(['[]' for _ in page])
            result += page_str + '\n' + page_sep + '\n'

        return result



album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())