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


from datetime import datetime, timezone

from ethereumetl.service.graph_operations import GraphOperations, OutOfBoundsError, Point


class EthService(object):
    def __init__(self, web3):
        graph = BlockTimestampGraph(web3)
        self._graph_operations = GraphOperations(graph)

    def get_block_range_for_date(self, date):
        pass

    def get_block_range_for_timestamps(self, start_timestamp, end_timestamp):
        pass


class BlockTimestampGraph(object):
    def __init__(self, web3):
        self._web3 = web3

    def get_first_point(self):
        # Ignore the genesis block as its timestamp is 0
        pass

    def get_last_point(self):
        pass

    def get_point(self, x):
        pass


def block_to_point(block):
    pass
