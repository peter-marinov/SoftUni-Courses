class DecorationRepository:
    def __init__(self):
        self.decorations: list = [] # obj from decorations

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        decoration_found = [d for d in self.decorations if type(d).__name__ == decoration_type]
        if decoration_found:
            return decoration_found[0]
        return 'None'

