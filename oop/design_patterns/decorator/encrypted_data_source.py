from design_patterns.decorator.data_source import DataSource


class EncryptedDataSource(DataSource):
    def __init__(self, count):
        self.data = []
        self.count = count

    def read(self):
        return '\n'.join(self.data)

    def write(self, data):
        encrypted_data = self.__encrypt_data(data)
        self.data.append(encrypted_data)

    def __encrypt_data(self, data):
        return ''.join(chr(ord(x) + self.count) for x in data)