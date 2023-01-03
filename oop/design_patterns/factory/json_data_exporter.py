import json

from design_patterns.factory.data_exporter import DataExporter


class JsonDataExporter(DataExporter):
    def export(self, data):
        return json.dumps(data)