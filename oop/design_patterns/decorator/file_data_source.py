from design_patterns.decorator.data_source import DataSource


class FileDataSource(DataSource):
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'r') as file:
            return file.read()

    def write(self, data):
        with open(self.path, 'a') as file:
            file.write(data + '\n')
            