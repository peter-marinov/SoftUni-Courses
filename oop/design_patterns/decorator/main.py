from design_patterns.decorator.file_data_source import FileDataSource
from design_patterns.decorator.encrypted_data_source import EncryptedDataSource
from design_patterns.decorator.encrypted_file_data_source import EncryptedDataSource

# file_data_source = FileDataSource('./result.txt')
# file_data_source.write('Hello world1')
# file_data_source.write('Hello world2')
# print(file_data_source.read())

# encrypted_data_source = EncryptedDataSource(10)
# encrypted_data_source.write('Hello world')
# print(encrypted_data_source.read())

data_source = EncryptedDataSource(10, "./result.txt")
data_source.write('Hello')
print(data_source.read())