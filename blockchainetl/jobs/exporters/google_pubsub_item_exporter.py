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

import json
import logging

from google.cloud import pubsub_v1
from timeout_decorator import timeout_decorator


class GooglePubSubItemExporter:

    def __init__(self, item_type_to_topic_mapping, message_attributes=(),
            batch_max_bytes=1024 * 5, batch_max_latency=1, batch_max_messages=1000,
            enable_message_ordering=False):
        self.item_type_to_topic_mapping = item_type_to_topic_mapping

        self.batch_max_bytes = batch_max_bytes
        self.batch_max_latency = batch_max_latency
        self.batch_max_messages = batch_max_messages

        self.enable_message_ordering = enable_message_ordering

        self.publisher = self.create_publisher()

        self.message_attributes = message_attributes

    def open(self):
        pass

    def export_items(self, items):
        pass

    @timeout_decorator.timeout(300)
    def _export_items_with_timeout(self, items):
        pass

    def export_item(self, item):
        pass

    def get_message_attributes(self, item):
        pass

    def create_publisher(self):
        pass

    def close(self):
        pass
