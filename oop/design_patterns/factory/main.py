from design_patterns.factory import data_exporter
from design_patterns.factory.data_exporter_factory import DataExporterFactory

data_exporter_factory = DataExporterFactory()

type = input()

data_Exporter = data_exporter_factory.create_exporter(type)
print(data_Exporter)
print(data_Exporter.export('Hello World'))