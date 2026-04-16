import collections
import json
import logging

from kafka import KafkaProducer

from blockchainetl.jobs.exporters.converters.composite_item_converter import CompositeItemConverter


class KafkaItemExporter:

    def __init__(self, output, item_type_to_topic_mapping, converters=()):
        self.item_type_to_topic_mapping = item_type_to_topic_mapping
        self.converter = CompositeItemConverter(converters)
        self.connection_url = self.get_connection_url(output)
        print(self.connection_url)
        self.producer = KafkaProducer(bootstrap_servers=self.connection_url)

    def get_connection_url(self, output):
        pass

    def open(self):
        pass

    def export_items(self, items):
        pass

    def export_item(self, item):
        pass

    def convert_items(self, items):
        pass

    def close(self):
        pass


def group_by_item_type(items):
    pass
