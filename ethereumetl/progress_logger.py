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
from datetime import datetime

from ethereumetl.atomic_counter import AtomicCounter


# Thread safe progress logger.
class ProgressLogger:
    def __init__(self, name='work', logger=None, log_percentage_step=10, log_item_step=5000):
        self.name = name
        self.total_items = None

        self.start_time = None
        self.end_time = None
        self.counter = AtomicCounter()
        self.log_percentage_step = log_percentage_step
        self.log_items_step = log_item_step
        if logger is not None:
            self.logger = logger
        else:
            self.logger = logging.getLogger('ProgressLogger')

    def start(self, total_items=None):
        pass

    # A race condition is possible where a message for the same percentage is printed twice, but it's a minor issue
    def track(self, item_count=1):
        pass

    def finish(self):
        pass
