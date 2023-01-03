from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass