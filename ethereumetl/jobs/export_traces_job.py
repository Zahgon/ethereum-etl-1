# MIT License
#
# Copyright (c) 2018 Evgeniy Filatov, evgeniyfilatov@gmail.com
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

from ethereumetl.executors.batch_work_executor import BatchWorkExecutor
from blockchainetl.jobs.base_job import BaseJob
from ethereumetl.mainnet_daofork_state_changes import DAOFORK_BLOCK_NUMBER
from ethereumetl.mappers.trace_mapper import EthTraceMapper
from ethereumetl.service.eth_special_trace_service import EthSpecialTraceService

from ethereumetl.service.trace_id_calculator import calculate_trace_ids
from ethereumetl.service.trace_status_calculator import calculate_trace_statuses
from ethereumetl.utils import validate_range


class ExportTracesJob(BaseJob):
    def __init__(
            self,
            start_block,
            end_block,
            batch_size,
            web3,
            item_exporter,
            max_workers,
            include_genesis_traces=False,
            include_daofork_traces=False):
        validate_range(start_block, end_block)
        self.start_block = start_block
        self.end_block = end_block

        self.web3 = web3

        # TODO: use batch_size when this issue is fixed https://github.com/paritytech/parity-ethereum/issues/9822
        self.batch_work_executor = BatchWorkExecutor(1, max_workers)
        self.item_exporter = item_exporter

        self.trace_mapper = EthTraceMapper()

        self.special_trace_service = EthSpecialTraceService()
        self.include_genesis_traces = include_genesis_traces
        self.include_daofork_traces = include_daofork_traces

    def _start(self):
        pass

    def _export(self):
        pass

    def _export_batch(self, block_number_batch):
        # TODO: Change to len(block_number_batch) > 0 when this issue is fixed
        # https://github.com/paritytech/parity-ethereum/issues/9822
        pass

    def _end(self):
        pass


def calculate_trace_indexes(traces):
    # Only works if traces were originally ordered correctly which is the case for Parity traces
    pass
