from design_patterns.factory.csv_data_exporter import CSVDataExporter
from design_patterns.factory.json_data_exporter import JsonDataExporter


class DataExporterFactory:
    def create_exporter(self, type):
        if type == 'json':
            return JsonDataExporter()
        elif type == 'csv':
            return CSVDataExporter()