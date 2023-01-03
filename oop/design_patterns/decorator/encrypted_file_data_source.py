from design_patterns.decorator.file_data_source import FileDataSource


class EncryptedDataSource(FileDataSource):
    def __init__(self, power, path):
        super().__init__(path)
        self.power = power

    def write(self, data):
        encrypted_data = self.__encrypt_data(data)
        super().write(encrypted_data)

    def __encrypt_data(self, data):
        return ''.join(chr(ord(x) + self.power) for x in data)