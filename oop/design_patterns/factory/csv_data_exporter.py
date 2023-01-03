from design_patterns.factory.data_exporter import DataExporter


class CSVDataExporter(DataExporter):
    def export(self, data):
        return data
