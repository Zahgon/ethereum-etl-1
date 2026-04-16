# MIT License
#
# Copyright (c) 2018 Evgeny Medvedev, evge.medvedev@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import logging

from blockchainetl.atomic_counter import AtomicCounter
from blockchainetl.exporters import CsvItemExporter, JsonLinesItemExporter
from blockchainetl.file_utils import get_file_handle, close_silently
from blockchainetl.jobs.exporters.converters.composite_item_converter import CompositeItemConverter


class CompositeItemExporter:
    def __init__(self, filename_mapping, field_mapping=None, converters=()):
        self.filename_mapping = filename_mapping
        self.field_mapping = field_mapping or {}

        self.file_mapping = {}
        self.exporter_mapping = {}
        self.counter_mapping = {}

        self.converter = CompositeItemConverter(converters)

        self.logger = logging.getLogger('CompositeItemExporter')

    def open(self):
        pass

    def export_items(self, items):
        pass

    def export_item(self, item):
        pass

    def close(self):
        pass
